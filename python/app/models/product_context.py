from dataclasses import dataclass, field, asdict


@dataclass
class ProductContext:

    produto: dict = field(default_factory=dict)

    videos: list = field(default_factory=list)

    consultas: list = field(default_factory=list)

    score_produto: float = 0

    metadata: dict = field(default_factory=dict)

    pipeline: dict = field(default_factory=dict)

    ia: dict = field(default_factory=dict)

    publicacao: dict = field(default_factory=dict)

    def to_dict(self):

        return asdict(self)