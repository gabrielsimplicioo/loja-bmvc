import json
import os

from app.models.exceptions import CredenciaisInvalidasError
from app.models.usuario import Usuario

DATA_FILE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'usuarios.json')
)


class UsuarioRepository:
    """Persiste usuarios administrativos em arquivo JSON e confere login.

    Segue o mesmo padrao do ProdutoRepository (Nivel II): sem banco de
    dados, com o arquivo criado e semeado automaticamente na primeira vez.
    """

    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self._garantir_arquivo()

    def _garantir_arquivo(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        if not os.path.exists(self.data_file):
            self._salvar(self._seed())

    def _seed(self):
        return [Usuario.criar(1, 'admin', 'technode123')]

    def _ler(self):
        with open(self.data_file, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return [Usuario.from_dict(item) for item in dados]

    def _salvar(self, usuarios):
        with open(self.data_file, 'w', encoding='utf-8') as arquivo:
            json.dump([u.to_dict() for u in usuarios], arquivo, ensure_ascii=False, indent=2)

    def autenticar(self, username, senha):
        username = (username or '').strip().lower()
        for usuario in self._ler():
            if usuario.username == username and usuario.senha_valida(senha):
                return usuario
        raise CredenciaisInvalidasError('Usuario ou senha invalidos.')
