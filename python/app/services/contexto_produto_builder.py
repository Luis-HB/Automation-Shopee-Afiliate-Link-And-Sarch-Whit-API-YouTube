from models.contexto_produto import ContextoProduto


class ContextoProdutoBuilder:

    def __init__(self):

        self.contexto = ContextoProduto()

    # ==========================================================
    # Produto
    # ==========================================================

    def produto(self, produto):

        self.contexto.produto = produto.__dict__.copy()

        self.contexto.score_produto = getattr(
            produto,
            "score",
            0
        )

        return self

    # ==========================================================
    # Consultas
    # ==========================================================

    def add_consulta(self, consulta):

        self.contexto.consultas.append(consulta)

        return self

    def add_consultas(self, consultas):

        self.contexto.consultas.extend(consultas)

        return self

    # ==========================================================
    # Vídeos
    # ==========================================================

    def add_video(self, video):

        if hasattr(video, "__dict__"):

            self.contexto.videos.append(
                video.__dict__.copy()
            )

        else:

            self.contexto.videos.append(video)

        return self

    def add_videos(self, videos):

        for video in videos:

            self.add_video(video)

        return self

    # ==========================================================
    # Metadata
    # ==========================================================

    def metadata(self, **kwargs):

        self.contexto.metadata.update(kwargs)

        return self

    # ==========================================================
    # Pipeline
    # ==========================================================

    def pipeline(self, **kwargs):

        self.contexto.pipeline.update(kwargs)

        return self

    # ==========================================================
    # IA
    # ==========================================================

    def ia(self, **kwargs):

        self.contexto.ia.update(kwargs)

        return self

    # ==========================================================
    # Publicação
    # ==========================================================

    def publicacao(self, **kwargs):

        self.contexto.publicacao.update(kwargs)

        return self

    # ==========================================================
    # Erros
    # ==========================================================

    def erro(self, mensagem):

        if "erros" not in self.contexto.metadata:

            self.contexto.metadata["erros"] = []

        self.contexto.metadata["erros"].append(mensagem)

        return self

    # ==========================================================
    # Build
    # ==========================================================

    def build(self):

        self.contexto.metadata.setdefault(
            "total_consultas",
            len(self.contexto.consultas)
        )

        self.contexto.metadata.setdefault(
            "total_videos",
            len(self.contexto.videos)
        )

        if self.contexto.videos:

            maior_score = max(

                video.get("score", 0)

                for video in self.contexto.videos

            )

        else:

            maior_score = 0

        self.contexto.metadata.setdefault(

            "melhor_score_video",

            maior_score

        )

        return self.contexto