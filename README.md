# 📋 API de Gerenciamento de Usuários e Enquetes - Back-end
---
## Descrição
Este é o back-end da aplicação, desenvolvido usando Django e Django REST Framework, com suporte a PostgreSQL. Ele fornece uma API RESTful para o front-end consumir, incluindo endpoints para cadastro e gerenciamento de usuários e enquetes.

## 🛠 Ferramentas Utilizadas
1. Django: Framework web para o back-end.
2. Django REST Framework: Extensão para criar APIs RESTful.
3. PostgreSQL: Banco de dados relacional.
4. Git: Controle de versão.
5. Postman: Ferramenta para testar APIs.

## 🚀 Como Rodar o Projeto Back-end
1. Clone o Repositório do Back-end
- git clone https://github.com/mathdourado01/Gerenciamento-de-Votos.git
- cd backend
2. Criar o Ambiente Virtual e Instalar Dependências
- python -m venv venv
- source venv/bin/activate  # No Windows: venv\Scripts\activate
- pip install -r requirements.txt
3. Configurar o Banco de Dados PostgreSQL
Crie o banco de dados no PostgreSQL e atualize as credenciais no arquivo settings.py.
4. Rodar as Migrações
- python manage.py migrate
5. Rodar o Servidor
- python manage.py runserver
Endpoints Disponíveis
POST /api/users/: Cadastrar novo usuário.
GET /api/users/: Listar todos os usuários.
(Futuro) POST /api/enquetes/: Criar nova enquete.
📚 Próximos Passos
Implementar endpoints para enquetes.
Melhorar a autenticação com tokens JWT.
