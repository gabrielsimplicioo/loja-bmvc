from bottle import template


class ControllerBase:
    """Controlador base da aplicacao.

    Concentra o utilitario de renderizacao de views para que os controllers
    concretos (Application, ProdutosController) nao dupliquem a chamada a
    bottle.template — heranca evitando repeticao de codigo.
    """

    def render_view(self, caminho, **contexto):
        return template(caminho, **contexto)
