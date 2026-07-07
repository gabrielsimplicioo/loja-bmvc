from app.controllers.application import Application
from app.controllers.produtos_controller import ProdutosController
from bottle import Bottle, run, static_file


app = Bottle()
ctl = Application()
produtos_ctl = ProdutosController()


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

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080, debug=True, reloader=True)
