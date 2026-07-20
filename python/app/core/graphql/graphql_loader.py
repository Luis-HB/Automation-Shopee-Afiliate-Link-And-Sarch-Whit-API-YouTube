from pathlib import Path


class GraphQLLoader:

    BASE_PATH = (
        Path(__file__).resolve().parents[2]
        / "graphql"
    )

    @classmethod
    def load(cls, filename):

        arquivo = cls.BASE_PATH / filename

        if not arquivo.exists():
            raise FileNotFoundError(
                f"GraphQL não encontrado: {arquivo}"
            )

        with open(
            arquivo,
            "r",
            encoding="utf-8"
        ) as f:

            return f.read()