from dataclasses import dataclass, field, asdict


@dataclass
class CommercialContext:

    #
    # Produto
    #
    product: dict = field(default_factory=dict)

    #
    # Análise comercial do produto
    #
    product_analysis: dict = field(default_factory=dict)

    #
    # Análise dos vídeos
    #
    video_analysis: dict = field(default_factory=dict)

    #
    # Análise do ranking
    #
    ranking_analysis: dict = field(default_factory=dict)

    #
    # Análise de mercado
    #
    market_analysis: dict = field(default_factory=dict)

    #
    # Consultas realizadas
    #
    queries: list = field(default_factory=list)

    #
    # Vídeos encontrados
    #
    videos: list = field(default_factory=list)

    #
    # Metadados
    #
    metadata: dict = field(default_factory=dict)

    def to_dict(self):

        return asdict(self)