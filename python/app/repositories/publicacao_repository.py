from repositories.repository import Repository
from models.publicacao import Publicacao


class PublicacaoRepository(Repository):

    def __init__(self):

        super().__init__(
            "publicacoes",
            Publicacao
        )