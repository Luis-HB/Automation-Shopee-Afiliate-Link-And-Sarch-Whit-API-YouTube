from repositories.base_repository import Repository
from models.publication import Publication


class PublicationRepository(Repository):

    def __init__(self):

        super().__init__(
            "publicacoes",
            Publication
        )