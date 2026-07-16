from pathlib import Path


class GraphQLLoader:

    BASE_PATH = Path(__file__).resolve().parent.parent / "graphql"

    @classmethod
    def load(cls, filename):

        arquivo = cls.BASE_PATH / filename

        with open(
            arquivo,
            "r",
            encoding="utf-8"
        ) as f:

            return f.read()