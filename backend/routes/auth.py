from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from database import get_db
from models.user import User
import os

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = os.getenv("SECRET_KEY", "thrive_secret_key_2024")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

class CadastroSchema(BaseModel):
    nome: str
    email: str
    senha: str
    nivel: str = "iniciante"

class LoginSchema(BaseModel):
    email: str
    senha: str

def criar_token(dados: dict):
    dados_copia = dados.copy()
    expira = datetime.utcnow() + timedelta(hours=24)
    dados_copia.update({"exp": expira})
    return jwt.encode(dados_copia, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/cadastro")
def cadastro(dados: CadastroSchema, db: Session = Depends(get_db)):
    usuario_existente = db.query(User).filter(User.email == dados.email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    senha_hash = pwd_context.hash(dados.senha)
    novo_usuario = User(
        nome=dados.nome,
        email=dados.email,
        senha_hash=senha_hash,
        nivel=dados.nivel
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return {"mensagem": "Usuário cadastrado com sucesso!", "id": novo_usuario.id}

@router.post("/login")
def login(dados: LoginSchema, db: Session = Depends(get_db)):
    usuario = db.query(User).filter(User.email == dados.email).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")
    
    if not pwd_context.verify(dados.senha, usuario.senha_hash):
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")
    
    token = criar_token({"sub": usuario.id, "email": usuario.email})
    return {
        "token": token,
        "nome": usuario.nome,
        "nivel": usuario.nivel,
        "xp_total": usuario.xp_total
    }
