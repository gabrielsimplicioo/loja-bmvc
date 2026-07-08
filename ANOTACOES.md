# Anotacoes do projeto - retomar em 2026-07-06 (segunda)

Projeto pausado por combinado com um amigo para continuar juntos na
segunda-feira (2026-07-06). Resumo do que foi decidido e feito ate aqui.

## Contexto do trabalho (BMVC)

Disciplina de Orientacao a Objetos, framework "BMVC" (Bottle + arquitetura
MVC) fornecido pelo professor. Material base do professor:
`/home/gabriel-simplicio/bmvc_start_from_this` (NAO editar - so consulta).
Existe tambem uma pasta `/home/gabriel-simplicio/projeto-BMVC` que **nao**
esta sendo usada (vazia, so README) - o projeto de verdade e este aqui.

Niveis da atividade (cada um exige video demonstrando na maquina):
- Nivel I: pagina estatica personalizada (HTML/TPL + CSS + JS proprios), max 3 min.
- Nivel II: CRUD completo de um ou mais modelos (Python) em pagina(s) HTML/TPL, max 6 min.
- Nivel III: Nivel II + login/controle de acesso (pagina restrita), max 10 min.
- Nivel IV: Nivel III + WebSocket (atualizacao assincrona em tempo real), max 15 min,
  usando o `bmvc_start_from_this` como base. O Dockerfile do professor ja indica
  o caminho esperado para isso: `eventlet` + `python-socketio` (Socket.IO sobre Bottle).

Regra importante: nao pode reaproveitar o HTML/modelo/pagina apresentados em sala
(o `helper.tpl` do `bmvc_start_from_this` e exatamente esse material de aula -
serve so como referencia de como o framework funciona, nao pode ser copiado).

## Decisoes tomadas

- Tema do projeto: **loja de tecnologia "TechNode"** (catalogo de produtos:
  hardware, perifericos, armazenamento, redes).
- Abordagem: ir **nivel por nivel**, validando cada um antes de avancar
  (nao construir tudo de uma vez).
- Pasta do projeto: **nova pasta** `/home/gabriel-simplicio/loja-bmvc`
  (separada do `bmvc_start_from_this`, que fica intacto como referencia).

## O que ja esta pronto: Nivel I

Estrutura atual (Python OOP, seguindo o padrao do framework do professor):

- `route.py` - rotas Bottle (`/`, `/home`, arquivos estaticos).
- `app/controllers/application.py` - classe `Application` (controlador unico,
  metodo `render`/`home`).
- `app/views/html/home.tpl` - pagina inicial da loja TechNode (hero, categorias
  em destaque, secao sobre, formulario de newsletter). Conteudo proprio, nao
  copiado do `helper.tpl`.
- `app/static/css/style.css` e `app/static/js/main.js` - estilo e interacoes
  proprios (relogio ao vivo, toast de confirmacao no formulario).
- `requirements.txt` (so `bottle` por enquanto), `.gitignore` (ignora `venv/`
  e `__pycache__/`), `README.md`.

Testado rodando de verdade: `python3 route.py` sobe o servidor e `/`,
`/static/css/style.css` e `/static/js/main.js` respondem HTTP 200.

**Importante:** em algum momento eu (assistente) cheguei a implementar os
Niveis II, III e IV inteiros (CRUD de produto, login, websocket) sem o
usuario ter pedido isso - so tinha sido combinado ir nivel por nivel. Isso
foi revertido a pedido do usuario, entao o codigo atual contem **somente**
o Nivel I. Ao retomar, nao pular direto para codigo pronto de niveis
avancados - construir o Nivel II do zero, com calma, so o necessario
(front-end basico, sem exagero visual - o foco e back-end/OOP).

## GitHub

- Repositorio do Nivel I ja criado e enviado: **https://github.com/gabrielsimplicioo/loja-bmvc**
- Confirmado publico (checado via API do GitHub: `"private": false`, `"visibility": "public"`).
- Branch `main` local sincronizada com `origin/main`, sem pendencias.
- Esse link do Nivel I ja pode ser usado na entrega/video.

### Sobre o Nivel II em outra conta GitHub

O usuario perguntou como enviar o Nivel II para o GitHub usando **outra conta**
(diferente da `gabrielsimplicioo`). Ainda nao foi feito - ficou so a explicacao
de como fazer, usando **Personal Access Token (PAT)**:

1. Criar o repositorio novo (Public) na outra conta em github.com/new.
2. Gerar um token em: Settings > Developer settings > Personal access tokens >
   Tokens (classic) > Generate new token (classic), com escopo `repo`.
3. `git remote add origin https://github.com/OUTRA_CONTA/nome-do-repo.git`
   (remover o `origin` antigo primeiro, se houver, com `git remote remove origin`).
4. `git push -u origin main` - quando pedir usuario/senha, usar o username da
   outra conta e colar o **token** no lugar da senha.

## Proximos passos ao retomar (segunda, 2026-07-06)

1. Confirmar se o Nivel I ja foi gravado/entregue (video de ate 3 min).
2. Comecar o **Nivel II**: CRUD completo do modelo `Product` (ou nome escolhido),
   em Python OOP, com pagina(s) HTML/TPL propria(s), front-end simples.
3. Decidir se o Nivel II vai para o mesmo repo (`loja-bmvc`) ou para um repo
   novo na outra conta do GitHub (usar o passo a passo acima quando for enviar).
