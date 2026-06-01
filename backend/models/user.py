from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from database import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha_hash = Column(String, nullable=False)
    nivel = Column(String, default="iniciante")
    xp_total = Column(Integer, default=0)
    criado_em = Column(DateTime, server_default=func.now())
    