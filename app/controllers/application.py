from app.controllers.controller_base import ControllerBase


class Application(ControllerBase):
    """Controlador da pagina inicial."""

    def __init__(self):
        self.pages = {
            'home': self.home,
        }

    def render(self, page, parameter=None):
        content = self.pages.get(page, self.home)
        if not parameter:
            return content()
        return content(parameter)

    def home(self):
        return self.render_view('app/views/html/home')
