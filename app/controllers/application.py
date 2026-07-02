from bottle import template


class Application():
    """Controlador principal da loja TechNode (nivel 1)."""

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
        return template('app/views/html/home')
