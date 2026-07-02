from app.controllers.application import Application
from bottle import Bottle, run, static_file


app = Bottle()
ctl = Application()


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

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080, debug=True, reloader=True)
