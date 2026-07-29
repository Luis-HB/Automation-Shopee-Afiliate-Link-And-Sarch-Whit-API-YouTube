from dataclasses import dataclass, field, asdict
from models.product import Product

@dataclass
class ProductContext:

    produto: Product = None

    consultas: list = field(default_factory=list)

    resultados: list = field(default_factory=list)

    videos: list = field(default_factory=list)

    score_produto: float = 0

    metadata: dict = field(default_factory=dict)

    pipeline: dict = field(default_factory=dict)

    ia: dict = field(default_factory=dict)

    publicacao: dict = field(default_factory=dict)