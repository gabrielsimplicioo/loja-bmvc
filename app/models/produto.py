from app.models.categoria import Categoria
from app.models.exceptions import ProdutoInvalidoError


class Produto:
    """Representa um produto do catalogo da TechNode.

    Os atributos sao protegidos por properties: nenhum Produto invalido
    consegue existir em memoria, pois cada setter valida o proprio dado
    antes de aceita-lo (encapsulamento).
    """

    def __init__(self, id, nome, categoria, preco, estoque, descricao=''):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque
        self.descricao = descricao

    # --- nome ---------------------------------------------------------

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        valor = (valor or '').strip()
        if not valor:
            raise ProdutoInvalidoError('O nome do produto e obrigatorio.')
        self._nome = valor

    # --- categoria ------------------------------------------------------

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        if isinstance(valor, Categoria):
            self._categoria = valor
            return
        try:
            self._categoria = Categoria.from_valor(valor)
        except ValueError as erro:
            raise ProdutoInvalidoError('Selecione uma categoria valida.') from erro

    # --- preco ----------------------------------------------------------

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        try:
            valor = float(str(valor).replace(',', '.'))
        except (TypeError, ValueError) as erro:
            raise ProdutoInvalidoError('Informe um preco valido.') from erro
        if valor < 0:
            raise ProdutoInvalidoError('O preco nao pode ser negativo.')
        self._preco = valor

    @property
    def preco_formatado(self):
        texto = f'{self._preco:,.2f}'.replace(',', '#').replace('.', ',').replace('#', '.')
        return f'R$ {texto}'

    # --- estoque --------------------------------------------------------

    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, valor):
        try:
            valor = int(valor)
        except (TypeError, ValueError) as erro:
            raise ProdutoInvalidoError('Informe uma quantidade em estoque valida.') from erro
        if valor < 0:
            raise ProdutoInvalidoError('O estoque nao pode ser negativo.')
        self._estoque = valor

    # --- descricao --------------------------------------------------------

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, valor):
        self._descricao = (valor or '').strip()

    # --- serializacao / representacao --------------------------------------

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self._nome,
            'categoria': self._categoria.value,
            'preco': self._preco,
            'estoque': self._estoque,
            'descricao': self._descricao,
        }

    @staticmethod
    def from_dict(dados):
        return Produto(
            id=dados['id'],
            nome=dados['nome'],
            categoria=dados['categoria'],
            preco=dados['preco'],
            estoque=dados['estoque'],
            descricao=dados.get('descricao', ''),
        )

    def __eq__(self, outro):
        if not isinstance(outro, Produto):
            return NotImplemented
        return self.id == outro.id

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f'Produto(id={self.id!r}, nome={self._nome!r}, categoria={self._categoria!r})'

    def __str__(self):
        return f'{self._nome} ({self._categoria.value})'
