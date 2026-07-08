from functools import wraps

from bottle import redirect, request, template

SECRET_KEY = 'technode-bmvc-chave-sessao'


class ControllerBase:

    def usuario_logado(self):
        return request.get_cookie('usuario', secret=SECRET_KEY)

    def render_view(self, caminho, **contexto):
        contexto.setdefault('usuario_logado', self.usuario_logado())
        return template(caminho, **contexto)


def login_obrigatorio(metodo):
    """Decorator: bloqueia acoes restritas quando nao ha sessao ativa."""

    @wraps(metodo)
    def wrapper(self, *args, **kwargs):
        if not self.usuario_logado():
            return redirect('/login')
        return metodo(self, *args, **kwargs)

    return wrapper
