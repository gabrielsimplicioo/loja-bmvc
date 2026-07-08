from abc import ABC, abstractmethod


class RepositorioBase(ABC):
    """Contrato que todo repositorio de produtos precisa seguir."""

    @abstractmethod
    def listar(self):
        ...

    @abstractmethod
    def buscar(self, id):
        ...

    @abstractmethod
    def criar(self, nome, categoria, preco, estoque, descricao):
        ...

    @abstractmethod
    def atualizar(self, id, nome, categoria, preco, estoque, descricao):
        ...

    @abstractmethod
    def excluir(self, id):
        ...
