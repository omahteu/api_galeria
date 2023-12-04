# API Galeria de Fotos

 ## Descrição
Este projeto consiste em uma API RESTful desenvolvida com Django REST Framework, proporcionando funcionalidades de registro de usuários, login, logout autenticados e upload de arquivos. A API foi projetada para oferecer uma solução escalável e segura para gerenciar usuários e manipular arquivos de maneira eficiente.

## Configuração
### Requisitos

#### Postgresql

Dados do Banco de Dados
- host: localhost
- user: postgres
- password: 123
- database: argo
- port: 5432

#### Django Rest Framework

Certifique-se de ter as seguintes dependências instaladas:

* Python (versão >= 3.x)
* Instale as dependências do projeto executando:

```
pip install requirements.txt
```

### Configuração de Ambiente

1. Clone este repositório
```
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

```
2. Crie e ative um ambiente virtual:
```
python -m venv venv
source venv/bin/activate  # No Windows, use venv\Scripts\activate.bat

```
3. Execute as migrações do banco de dados:
```
python manage.py migrate
```
4. Inicie o servidor:
```
python manage.py runserver
```

## Endpoints

Registro de Usuário: POST /api/register/
 * Parâmetros
   * username (string): Nome de usuário único.
   * password (string): Senha do usuário.
   * password (string): Email do usuário.
Login: POST /api/login/
 * Parâmetros
    * username (string): Nome de usuário registrado.
    * password (string): Senha do usuário registrado.
Logout: POST /api/logout/
Upload de Arquivo (requer autenticação): POST /api/upload/
 * Parâmetros
  * Token
  * imagem
  * titulo
  * comentario
