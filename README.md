# Arquivos
- docker-compose.yml
- database.py
- models.py
- schemas.py
- main.py
- .env
## Docker Compose
Sobe o postgreSQL localmente sem instalar nada na máquina.
## Conexão com SQL Alchemy
Criar, engine, sessão e Base declarativa para os modelos.
## Modelos ORM
Classes Python mapeadas para tabelas do banco de dados.
## Migrations com Alembic
Controle de versão do schema do banco, sem perder dados.
## Rotas CRUD com o FastAPI
Endpoints que lêem e escrevem no banco de dados usando a sessão do SQL Alchemy.