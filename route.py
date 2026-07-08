import os

from app.controllers.application import Application
from app.controllers.auth_controller import AuthController
from app.controllers.produtos_controller import ProdutosController
from app.tempo_real.servidor_estoque import ServidorEstoque
from bottle import Bottle, run, static_file

RELOADER = True
WEBSOCKET_PORTA = 8081

app = Bottle()
servidor_estoque = ServidorEstoque(porta=WEBSOCKET_PORTA)
ctl = Application()
produtos_ctl = ProdutosController(servidor_estoque)
auth_ctl = AuthController()


#-----------------------------------------------------------------------------
# Arquivos estaticos (CSS, JS, imagens)

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')


#-----------------------------------------------------------------------------
# Rotas da loja TechNode

@app.route('/', method='GET')
@app.route('/home', method='GET')
def home():
    return ctl.render('home')


#-----------------------------------------------------------------------------
# CRUD de produtos (BMVC Nivel II)

@app.route('/produtos', method='GET')
def produtos_index():
    return produtos_ctl.index()


@app.route('/produtos/novo', method='GET')
def produtos_novo():
    return produtos_ctl.novo()


@app.route('/produtos', method='POST')
def produtos_criar():
    return produtos_ctl.criar()


@app.route('/produtos/<id:int>/editar', method='GET')
def produtos_editar(id):
    return produtos_ctl.editar(id)


@app.route('/produtos/<id:int>', method='POST')
def produtos_atualizar(id):
    return produtos_ctl.atualizar(id)


@app.route('/produtos/<id:int>/excluir', method='POST')
def produtos_excluir(id):
    return produtos_ctl.excluir(id)


#-----------------------------------------------------------------------------
# Autenticacao (BMVC Nivel III)

@app.route('/login', method='GET')
def login_form():
    return auth_ctl.login_form()


@app.route('/login', method='POST')
def login():
    return auth_ctl.login()


@app.route('/logout', method='POST')
def logout():
    return auth_ctl.logout()


#-----------------------------------------------------------------------------

if __name__ == '__main__':
    # com reloader, o Bottle roda este arquivo de novo num processo filho, so ele abre o websocket
    if not RELOADER or os.environ.get('BOTTLE_CHILD'):
        servidor_estoque.iniciar()
    # waitress em vez do servidor padrao, que trava com varias abas abertas ao mesmo tempo
    run(app, server='waitress', host='0.0.0.0', port=8080, debug=True, reloader=RELOADER)
