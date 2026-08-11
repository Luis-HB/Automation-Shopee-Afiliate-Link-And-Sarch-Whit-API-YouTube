from dataclasses import dataclass, field, asdict


@dataclass
class CommercialDecision:

    # =====================================================
    # Resultado
    # =====================================================

    recommendation: str = "REJECT"

    publication_priority: int = 0

    confidence: float = 0.0

    estimated_conversion: float = 0.0

    # =====================================================
    # Vídeo escolhido
    # =====================================================

    best_video_id: int | None = None

    best_video_url: str = ""

    # =====================================================
    # Público
    # =====================================================

    audience: str = ""

    # =====================================================
    # Estratégia
    # =====================================================

    marketing_angle: str = ""

    # =====================================================
    # Explicação
    # =====================================================

    reason: str = ""

    # =====================================================
    # Critérios utilizados
    # =====================================================

    selection_criteria: dict = field(default_factory=dict)

    # =====================================================
    # Pontos positivos
    # =====================================================

    strengths: list = field(default_factory=list)

    weaknesses: list = field(default_factory=list)

    opportunities: list = field(default_factory=list)

    warnings: list = field(default_factory=list)

    recommendations: list = field(default_factory=list)

    # =====================================================

    raw_response: dict = field(default_factory=dict)

    # =====================================================

    @property
    def approved(self):

        return self.publication_priority >= 60

    # =====================================================

    def to_dict(self):

        return asdict(self)