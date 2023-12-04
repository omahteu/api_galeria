**Coleção do Postman para Django RESTful API**

---

## Importando a Coleção no Postman

1. Baixe o arquivo de coleção [Django_RESTful_API.postman_collection.json](#) para o seu computador.
2. Abra o Postman.
3. No canto superior esquerdo, clique em "Import".
4. Selecione a opção "Import File" e escolha o arquivo baixado.
5. A coleção "Django RESTful API" será adicionada à sua lista de coleções.

---

## Uso da Coleção

1. Certifique-se de que o servidor Django está em execução.
2. Abra a coleção "Django RESTful API" no Postman.

### Registro de Usuário

- **Rota:** `POST /api/register/`
- **Exemplo de Requisição:**
  ```json
  {
    "username": "seu_nome_de_usuario",
    "password": "sua_senha"
  }
  ```
- **Exemplo de Resposta de Sucesso:**
  ```json
  {
    "detail": "Usuário registrado com sucesso."
  }
  ```

### Login

- **Rota:** `POST /api/login/`
- **Exemplo de Requisição:**
  ```json
  {
    "username": "seu_nome_de_usuario",
    "password": "sua_senha"
  }
  ```
- **Exemplo de Resposta de Sucesso:**
  ```json
  {
    "token": "SEU_TOKEN"
  }
  ```

### Logout

- **Rota:** `POST /api/logout/`
- **Exemplo de Requisição:**
  - Necessário incluir o cabeçalho `Authorization: Token SEU_TOKEN`

- **Exemplo de Resposta de Sucesso:**
  ```json
  {
    "detail": "Logout realizado com sucesso."
  }
  ```

### Upload de Arquivo

- **Rota:** `POST /api/upload/`
- **Exemplo de Requisição:**
  - Necessário incluir o cabeçalho `Authorization: Token SEU_TOKEN`
  - Selecionar um arquivo para carregar no corpo da requisição.

- **Exemplo de Resposta de Sucesso:**
  ```json
  {
    "detail": "Upload de arquivo concluído com sucesso."
  }
  ```

---

## Observações

- Certifique-se de ajustar o URL base da API no ambiente do Postman para refletir o local onde sua aplicação está sendo executada (por exemplo, `http://127.0.0.1:8000`).

---

Sinta-se à vontade para adaptar ou expandir esta coleção conforme necessário para atender às suas necessidades específicas.
