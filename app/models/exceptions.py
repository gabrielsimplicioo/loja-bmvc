class TechNodeError(Exception):
    """Erro base de dominio da TechNode."""


class ProdutoInvalidoError(TechNodeError):
    """Levantado quando os dados de um produto violam alguma regra de negocio."""


class ProdutoNaoEncontradoError(TechNodeError):
    """Levantado quando um produto buscado por id nao existe no repositorio."""


class CredenciaisInvalidasError(TechNodeError):
    """Levantado quando o login e feito com usuario ou senha incorretos."""
