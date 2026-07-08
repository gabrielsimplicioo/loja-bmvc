# TechNode - Loja de Tecnologia (Projeto BMVC)

Projeto academico da disciplina de Orientacao a Objetos, construido sobre o
framework BMVC (Bottle + arquitetura MVC).

## Nivel I

Pagina inicial estatica da loja TechNode, com HTML/TPL, CSS e JS proprios
(sem reaproveitar o exemplo `helper` apresentado em sala).

## Nivel II

CRUD completo do model `Produto` (`app/models/produto.py`), persistido em
`data/produtos.json` (sem banco de dados). O catalogo fica disponivel em
`/produtos`, com paginas proprias de listagem e formulario
(`app/views/html/produtos/`), CSS proprio e um JS dedicado
(`app/static/js/produtos.js`) com confirmacao antes de excluir um produto.

Rotas do CRUD:

| Metodo | Rota                     | Acao                          |
|--------|--------------------------|--------------------------------|
| GET    | `/produtos`               | Lista produtos                 |
| GET    | `/produtos/novo`          | Formulario de cadastro         |
| POST   | `/produtos`                | Cria um produto                |
| GET    | `/produtos/<id>/editar`   | Formulario de edicao           |
| POST   | `/produtos/<id>`           | Atualiza um produto            |
| POST   | `/produtos/<id>/excluir`  | Remove um produto              |

## Nivel III

Controle de acesso sobre o mesmo CRUD do Nivel II: o catalogo (`/produtos`)
continua publico para visualizacao, mas cadastrar, editar e excluir produtos
passou a exigir login. A sessao e guardada em cookie assinado
(`app/controllers/controller_base.py`), sem servidor de sessao ou banco de
dados.

Conta padrao (semeada em `data/usuarios.json` na primeira execucao):

| Usuario | Senha         |
|---------|---------------|
| admin   | technode123   |

Rotas de autenticacao:

| Metodo | Rota      | Acao                          |
|--------|-----------|--------------------------------|
| GET    | `/login`  | Formulario de login            |
| POST   | `/login`  | Autentica e cria a sessao      |
| POST   | `/logout` | Encerra a sessao               |

As rotas `/produtos/novo`, `POST /produtos`, `/produtos/<id>/editar`,
`POST /produtos/<id>` e `/produtos/<id>/excluir` agora exigem sessao ativa
(decorator `login_obrigatorio`); sem login, o usuario e redirecionado para
`/login`.

## Nivel IV (atual)

O catalogo (`/produtos`) passou a atualizar sozinho, em tempo real, sem
recarregar a pagina. Sempre que um produto e criado, editado ou excluido,
o servidor avisa todo mundo que estiver com o catalogo aberto — inclusive
visitantes sem login.

Isso e feito com um servidor Websocket proprio
(`app/tempo_real/servidor_estoque.py`, classe `ServidorEstoque`), que roda
numa thread separada do Bottle, numa segunda porta (8081). O
`ProdutosController` recebe essa instancia por injecao de dependencia e,
apos cada operacao do CRUD, chama `avisar(...)`; o front-end
(`app/static/js/produtos.js`) mantem uma conexao Websocket aberta e
atualiza a tabela e o contador de visitantes na hora, sem F5.

Nenhum banco de dados ou fila externa foi adicionado: o Websocket so
transmite eventos, quem persiste os dados continua sendo o
`ProdutoRepository` (arquivo JSON).

## Como executar

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 route.py
```

Acesse: http://localhost:8080/
