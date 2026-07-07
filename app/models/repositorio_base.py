from abc import ABC, abstractmethod


class RepositorioBase(ABC):
    """Contrato que toda camada de persistencia de produtos deve seguir.

    Isola quem usa o repositorio (o controller) da forma como os dados sao
    guardados. Trocar a implementacao concreta (arquivo, banco, memoria)
    nao exige alterar quem a consome: basta que a nova classe herde daqui
    e implemente os mesmos metodos (polimorfismo).
    """

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
