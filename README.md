# 🌱 Thrive — Educação Financeira Gamificada

> Aprenda sobre finanças, invista com confiança e conecte-se com uma comunidade financeira. Tudo em um só lugar.

---

## 📱 Sobre o Projeto

O **Thrive** é um aplicativo de educação financeira com sistema de gamificação, missões diárias e rede social financeira. O objetivo é tornar o aprendizado sobre finanças acessível, engajante e progressivo — para iniciantes que estão começando do zero até investidores avançados que querem se manter atualizados.

---

## ✨ Funcionalidades

- 🎯 **Sistema de níveis** — Iniciante, Intermediário e Avançado
- 📚 **Lições de educação financeira** organizadas por nível
- ✅ **Missões diárias** com recompensas em XP
- 🌳 **Árvore evolutiva** com conquistas e badges
- 💬 **Rede social financeira** — feed, posts e comentários
- 📰 **Notícias do mercado financeiro** em tempo real
- 🧮 **Simulações** — juros compostos, metas e calculadoras
- 💡 **Dicas personalizadas** por perfil de usuário

---

## 🛠️ Stack Tecnológica

| Camada | Tecnologia |
|--------|-----------|
| Backend | Python · FastAPI · SQLAlchemy |
| Banco de dados | PostgreSQL (Supabase) |
| Frontend | React · HTML · CSS |
| Hospedagem | Vercel (frontend) · Railway (backend) |
| Autenticação | JWT (JSON Web Tokens) |
| Segurança | HTTPS · Rate limiting · Logs de acesso |

---

## 🗂️ Estrutura do Projeto

```
thrive/
├── backend/
│   ├── main.py           # Entrada da aplicação FastAPI
│   ├── database.py       # Conexão com o banco de dados
│   ├── models/           # Tabelas do banco (SQLAlchemy)
│   │   ├── user.py
│   │   ├── missao.py
│   │   ├── post.py
│   │   └── licao.py
│   ├── routes/           # Endpoints da API
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── missoes.py
│   │   └── posts.py
│   └── schemas/          # Validação de dados (Pydantic)
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   └── App.jsx
└── README.md
```

---

## 🚀 Como Rodar Localmente

### Pré-requisitos
- Python 3.11+
- Node.js 18+
- PostgreSQL ou conta no Supabase

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

---

## 🗺️ Roadmap

- [x] Planejamento e banco de dados
- [ ] Autenticação (cadastro e login)
- [ ] Sistema de missões e XP
- [ ] Lições por nível
- [ ] Árvore evolutiva e conquistas
- [ ] Rede social (feed e comentários)
- [ ] Notícias em tempo real
- [ ] Simulações financeiras
- [ ] Deploy em produção

---

## 👤 Autor

Desenvolvido por **[Diego Henrique]**


---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
