# TechNode

Loja de tecnologia feita para a disciplina de Orientação a Objetos, em cima do
framework BMVC (Bottle + MVC).

## Como rodar

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 route.py
```

Acesse http://localhost:8080/. O servidor sobe na porta 8080 e o websocket
(atualização em tempo real do catálogo) sobe junto, na 8081.

Login pra gerenciar produtos: `admin` / `technode123` (conta criada
automaticamente em `data/usuarios.json` na primeira execução).

## O que tem

- **Página inicial** (`/`) — estática, com CSS e JS próprios.
- **Catálogo de produtos** (`/produtos`) — CRUD completo, aberto pra visita
  mas só deixa cadastrar/editar/excluir quem estiver logado.
- **Login** (`/login`) — sessão guardada em cookie assinado, sem servidor de
  sessão nem banco de dados.
- **Tempo real** — quando alguém cria, edita ou remove um produto, o catálogo
  de todo mundo que estiver com a página aberta atualiza sozinho, sem F5.

Tudo persiste em JSON (`data/produtos.json`, `data/usuarios.json`), sem
banco de dados.

## Rotas

| Método | Rota                    | Ação                     |
|--------|-------------------------|--------------------------|
| GET    | `/`                     | Página inicial           |
| GET    | `/produtos`             | Lista produtos           |
| GET    | `/produtos/novo`        | Formulário de cadastro   |
| POST   | `/produtos`             | Cria um produto          |
| GET    | `/produtos/<id>/editar` | Formulário de edição     |
| POST   | `/produtos/<id>`        | Atualiza um produto      |
| POST   | `/produtos/<id>/excluir`| Remove um produto        |
| GET    | `/login`                | Formulário de login      |
| POST   | `/login`                | Autentica                |
| POST   | `/logout`               | Encerra a sessão         |

As rotas de cadastro/edição/exclusão de produto exigem login; sem sessão
ativa, redirecionam para `/login`.

## Estrutura

```
app/
  controllers/   # recebem a requisicao e chamam o model
  models/        # regras de negocio e persistencia (JSON)
  tempo_real/    # servidor websocket
  views/html/    # templates .tpl
  static/        # css e js
data/            # arquivos json (gerados na primeira execucao)
route.py         # define as rotas e sobe o servidor
```
