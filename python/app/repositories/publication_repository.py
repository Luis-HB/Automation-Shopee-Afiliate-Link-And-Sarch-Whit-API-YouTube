from repositories.repository import Repository
from python.app.models.publication import Publicacao


class PublicacaoRepository(Repository):

    def __init__(self):

        super().__init__(
            "publicacoes",
            Publicacao
        )