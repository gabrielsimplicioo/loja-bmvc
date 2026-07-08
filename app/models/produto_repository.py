import json
import os
from threading import Lock

from app.models.exceptions import ProdutoNaoEncontradoError
from app.models.produto import Produto
from app.models.repositorio_base import RepositorioBase

DATA_FILE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'produtos.json')
)


class ProdutoRepository(RepositorioBase):
    """Persiste e consulta produtos em um arquivo JSON (sem banco de dados).

    Implementa o contrato de RepositorioBase: e uma especializacao concreta
    (heranca) da abstracao definida na classe-mae.
    """

    _lock = Lock()

    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self._garantir_arquivo()

    def _garantir_arquivo(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        if not os.path.exists(self.data_file):
            self._salvar(self._seed())

    def _seed(self):
        return [
            Produto(1, 'RTX 4060 8GB', 'Hardware', 2199.90, 12,
                    'Placa de video para uso gamer e profissional.'),
            Produto(2, 'Teclado Mecanico ABNT2', 'Perifericos', 349.90, 25,
                    'Switches red, fio destacavel, retroiluminado.'),
            Produto(3, 'SSD NVMe 1TB', 'Armazenamento', 459.90, 30,
                    'Leitura sequencial de ate 3500MB/s.'),
            Produto(4, 'Roteador Wi-Fi 6 AX1800', 'Redes', 389.90, 15,
                    'Cobertura ampliada, ideal para home office.'),
        ]

    def _ler(self):
        with open(self.data_file, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return [Produto.from_dict(item) for item in dados]

    def _salvar(self, produtos):
        with open(self.data_file, 'w', encoding='utf-8') as arquivo:
            json.dump([p.to_dict() for p in produtos], arquivo, ensure_ascii=False, indent=2)

    def _encontrar(self, produtos, id):
        for produto in produtos:
            if produto.id == id:
                return produto
        raise ProdutoNaoEncontradoError(f'Produto {id} nao encontrado.')

    def listar(self):
        return sorted(self._ler(), key=lambda p: p.nome)

    def buscar(self, id):
        return self._encontrar(self._ler(), id)

    def criar(self, nome, categoria, preco, estoque, descricao):
        with self._lock:
            produtos = self._ler()
            novo_id = max([p.id for p in produtos], default=0) + 1
            produto = Produto(novo_id, nome, categoria, preco, estoque, descricao)
            produtos.append(produto)
            self._salvar(produtos)
            return produto

    def atualizar(self, id, nome, categoria, preco, estoque, descricao):
        with self._lock:
            produtos = self._ler()
            produto = self._encontrar(produtos, id)
            produto.nome = nome
            produto.categoria = categoria
            produto.preco = preco
            produto.estoque = estoque
            produto.descricao = descricao
            self._salvar(produtos)
            return produto

    def excluir(self, id):
        with self._lock:
            produtos = self._ler()
            produto = self._encontrar(produtos, id)
            produtos.remove(produto)
            self._salvar(produtos)
            return produto
