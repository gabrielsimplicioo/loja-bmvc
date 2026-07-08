import hashlib
import os


class Usuario:
    """Representa um usuario com acesso ao painel administrativo da TechNode.

    A senha nunca e guardada em texto puro: o proprio objeto sabe gerar
    (`criar`) e conferir (`senha_valida`) seu hash, escondendo os detalhes
    de hashing de quem o utiliza (encapsulamento).
    """

    def __init__(self, id, username, senha_hash, salt):
        self.id = id
        self.username = username
        self._senha_hash = senha_hash
        self._salt = salt

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, valor):
        self._username = (valor or '').strip().lower()

    @staticmethod
    def _hash(senha, salt):
        return hashlib.sha256(f'{salt}{senha}'.encode('utf-8')).hexdigest()

    @classmethod
    def criar(cls, id, username, senha):
        salt = os.urandom(16).hex()
        return cls(id, username, cls._hash(senha, salt), salt)

    def senha_valida(self, senha):
        return self._hash(senha, self._salt) == self._senha_hash

    def to_dict(self):
        return {
            'id': self.id,
            'username': self._username,
            'senha_hash': self._senha_hash,
            'salt': self._salt,
        }

    @staticmethod
    def from_dict(dados):
        return Usuario(dados['id'], dados['username'], dados['senha_hash'], dados['salt'])

    def __repr__(self):
        return f'Usuario(id={self.id!r}, username={self._username!r})'
