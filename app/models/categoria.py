from enum import Enum


class Categoria(Enum):
    """Categorias de produtos aceitas pelo catalogo da TechNode."""

    HARDWARE = 'Hardware'
    PERIFERICOS = 'Perifericos'
    ARMAZENAMENTO = 'Armazenamento'
    REDES = 'Redes'
    OUTROS = 'Outros'

    @classmethod
    def valores(cls):
        return [categoria.value for categoria in cls]

    @classmethod
    def from_valor(cls, valor):
        for categoria in cls:
            if categoria.value == valor:
                return categoria
        raise ValueError(f'Categoria invalida: {valor!r}')

    def __str__(self):
        return self.value
