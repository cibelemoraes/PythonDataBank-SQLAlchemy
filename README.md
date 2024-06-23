# Resumo do Projeto
## Este projeto consiste em uma aplicação web utilizando Flask e SQLAlchemy para gerenciamento de pessoas e suas atividades. Abaixo está um resumo das funcionalidades implementadas e as bibliotecas utilizadas.

### Bibliotecas Utilizadas
SQLAlchemy: Utilizada para mapear classes Python para tabelas do banco de dados e gerenciar consultas e transações.
Flask: Framework web utilizado para criar a aplicação web.
Flask-RESTful: Extensão do Flask para facilitar a criação de APIs RESTful.
Flask-HTTPAuth: Utilizada para autenticação básica HTTP.
###  Funcionalidades
### Configuração do Banco de Dados:

create_engine para criar a conexão com o banco de dados SQLite.
declarative_base para definir a base das classes mapeadas para o banco de dados.
sessionmaker e scoped_session para gerenciar sessões de banco de dados.

### Modelos:

Pessoas e Atividades são definidos como classes Python e mapeados para tabelas no banco de dados.
Métodos save e delete são adicionados para facilitar a manipulação de registros.

### Inicialização do Banco de Dados:

init_db para criar as tabelas no banco de dados a partir dos modelos definidos.

### API RESTful:

#### Pessoas:
GET /pessoa/<nome>: Retorna os dados de uma pessoa específica.
PUT /pessoa/<nome>: Atualiza os dados de uma pessoa.
DELETE /pessoa/<nome>: Exclui uma pessoa.
#### ListaPessoas:
GET /pessoa: Retorna uma lista de todas as pessoas.
POST /pessoa: Adiciona uma nova pessoa.
#### ListaAtividade:
GET /atividades: Retorna uma lista de todas as atividades.
POST /atividades: Adiciona uma nova atividade.

### Autenticação:

Implementada com Flask-HTTPAuth para proteger os endpoints, exigindo login e senha.

### Execução
Para executar a aplicação, basta rodar o arquivo principal:
python app.py
A aplicação estará disponível em http://127.0.0.1:5000

### Considerações Finais
Este projeto demonstra como criar uma API RESTful em Flask, utilizando SQLAlchemy para o gerenciamento de dados e implementando autenticação básica para segurança. É uma base sólida para projetos que envolvem CRUD e autenticação.
Projeto realizado por Cibele Gomes Domingos Moraes Lima 
