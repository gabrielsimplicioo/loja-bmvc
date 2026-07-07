from urllib.parse import quote

from bottle import redirect, request

from app.controllers.controller_base import ControllerBase
from app.models.categoria import Categoria
from app.models.exceptions import ProdutoInvalidoError, ProdutoNaoEncontradoError
from app.models.produto_repository import ProdutoRepository

MENSAGENS_FLASH = {
    'criado': ('ok', 'Produto cadastrado com sucesso.'),
    'atualizado': ('ok', 'Produto atualizado com sucesso.'),
    'excluido': ('ok', 'Produto removido do catalogo.'),
    'nao_encontrado': ('erro', 'Produto nao encontrado.'),
}


class ProdutosController(ControllerBase):
    """Controlador do CRUD de produtos da TechNode (BMVC Nivel II).

    Nao valida dados por conta propria: delega essa responsabilidade ao
    model (Produto), que e quem conhece as proprias regras de negocio.
    Aqui apenas orquestra o repositorio e traduz os erros de dominio em
    respostas HTTP.
    """

    def __init__(self):
        self.repo = ProdutoRepository()

    def index(self):
        produtos = self.repo.listar()
        tipo_flash, texto_flash = MENSAGENS_FLASH.get(request.query.msg, (None, None))
        return self.render_view(
            'app/views/html/produtos/index',
            produtos=produtos,
            tipo_flash=tipo_flash,
            texto_flash=texto_flash,
        )

    def novo(self):
        return self.render_view(
            'app/views/html/produtos/form',
            produto=None,
            categorias=Categoria.valores(),
            erro=request.query.erro or None,
        )

    def criar(self):
        dados = self._dados_formulario()
        try:
            self.repo.criar(**dados)
        except ProdutoInvalidoError as erro:
            return redirect(f'/produtos/novo?erro={quote(str(erro))}')
        return redirect('/produtos?msg=criado')

    def editar(self, id):
        try:
            produto = self.repo.buscar(id)
        except ProdutoNaoEncontradoError:
            return redirect('/produtos?msg=nao_encontrado')
        return self.render_view(
            'app/views/html/produtos/form',
            produto=produto,
            categorias=Categoria.valores(),
            erro=request.query.erro or None,
        )

    def atualizar(self, id):
        dados = self._dados_formulario()
        try:
            self.repo.atualizar(id, **dados)
        except ProdutoNaoEncontradoError:
            return redirect('/produtos?msg=nao_encontrado')
        except ProdutoInvalidoError as erro:
            return redirect(f'/produtos/{id}/editar?erro={quote(str(erro))}')
        return redirect('/produtos?msg=atualizado')

    def excluir(self, id):
        try:
            self.repo.excluir(id)
        except ProdutoNaoEncontradoError:
            pass
        return redirect('/produtos?msg=excluido')

    def _dados_formulario(self):
        return {
            'nome': request.forms.getunicode('nome', ''),
            'categoria': request.forms.getunicode('categoria', ''),
            'preco': request.forms.get('preco', ''),
            'estoque': request.forms.get('estoque', ''),
            'descricao': request.forms.getunicode('descricao', ''),
        }
