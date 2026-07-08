from urllib.parse import quote

from bottle import redirect, request, response

from app.controllers.controller_base import SECRET_KEY, ControllerBase
from app.models.exceptions import CredenciaisInvalidasError
from app.models.usuario_repository import UsuarioRepository


class AuthController(ControllerBase):
    """Controlador de login e logout."""

    def __init__(self):
        self.repo = UsuarioRepository()

    def login_form(self):
        return self.render_view('app/views/html/login', erro=request.query.erro or None)

    def login(self):
        username = request.forms.getunicode('username', '')
        senha = request.forms.get('senha', '')
        try:
            usuario = self.repo.autenticar(username, senha)
        except CredenciaisInvalidasError as erro:
            return redirect(f'/login?erro={quote(str(erro))}')
        response.set_cookie('usuario', usuario.username, secret=SECRET_KEY, path='/', httponly=True)
        return redirect('/produtos')

    def logout(self):
        response.delete_cookie('usuario', path='/')
        return redirect('/produtos')
