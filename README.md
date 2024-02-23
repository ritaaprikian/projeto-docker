## Projeto Docker - Ada Tech

## Descrição

Uma aplicação em Python
Banco de dados PostgreSQL
Para projeto docker utilizando docker-compose.yml

## Pré-requisitos

- Python 3.x instalado
- Docker e Docker Compose instalados (se estiver usando Docker)
- Conexão à Internet (para instalar dependências)

## Configuração do Ambiente
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydatabase

### Instalação das Dependências Python

```bash
pip install -r requirements.txt



##Rodando projeto docker
- Abra docker
- Abra VSCode
- Instale a extensão Thunder
- Rode docker-compose up -d     (não se esqueça de estar dentro da pasta do docker-compose)
- Utilize a extensão Thunder, inicie uma nova conexão, digite http://localhost:5000 e envie
- Agora mude para post, digite http://localhost:5000/enviar_dados e envie.
- Agora envie seus dados/mensagens para serem salvas no banco de dados.
- Instale a extensão SQL
- Selecione PostgreSQL
- Insira a senha: password
- Insira database: mydatabase
- Connect
- Dentro da pasta public/dados você terá acesso há todos dados salvos 
