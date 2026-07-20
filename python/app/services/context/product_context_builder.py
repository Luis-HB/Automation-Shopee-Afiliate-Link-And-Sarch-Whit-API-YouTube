from models.product_context import ContextoProduto


class ProductContextBuilder:

    def __init__(self):
        self.contexto = ProductContext()

    # ==========================================================
    # Product
    # ==========================================================

    def product(self, product):

        self.contexto.produto = product.__dict__.copy()

        self.contexto.score_produto = getattr(
            product,
            "score",
            0
        )

        return self

    # ==========================================================
    # Searches
    # ==========================================================

    def add_query(self, query):

        self.contexto.consultas.append(query)

        return self

    def add_queries(self, queries):

        self.contexto.consultas.extend(queries)

        return self

    # ==========================================================
    # Videos
    # ==========================================================

    def add_video(self, video):

        if hasattr(video, "__dict__"):
            self.contexto.videos.append(video.__dict__.copy())
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
    # AI
    # ==========================================================

    def ai(self, **kwargs):

        self.contexto.ia.update(kwargs)

        return self

    # ==========================================================
    # Publication
    # ==========================================================

    def publication(self, **kwargs):

        self.contexto.publicacao.update(kwargs)

        return self

    # ==========================================================
    # Errors
    # ==========================================================

    def error(self, message):

        self.contexto.metadata.setdefault("errors", [])

        self.contexto.metadata["errors"].append(message)

        return self

    # ==========================================================
    # Build
    # ==========================================================

    def build(self):

        self.contexto.metadata.setdefault(
            "total_queries",
            len(self.contexto.consultas)
        )

        self.contexto.metadata.setdefault(
            "total_videos",
            len(self.contexto.videos)
        )

        highest_score = max(
            (video.get("score", 0) for video in self.contexto.videos),
            default=0
        )

        self.contexto.metadata.setdefault(
            "best_video_score",
            highest_score
        )

        return self.contexto