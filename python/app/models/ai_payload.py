from dataclasses import dataclass, field, asdict
from datetime import datetime


from models.commercial.knowledge import Knowledge
from models.commercial.evidence import Evidence


@dataclass
class AIPayload:

    # =====================================================
    # Informações do Produto
    # =====================================================

    product: dict = field(default_factory=dict)

    # =====================================================
    # Conhecimento produzido pelo pipeline
    # =====================================================

    knowledge: Knowledge | None = None

    # =====================================================
    # Evidências utilizadas
    # =====================================================

    evidence: Evidence | None = None

    # =====================================================
    # Metadados do processamento
    # =====================================================

    metadata: dict = field(default_factory=dict)

    # =====================================================
    # Configuração do agente
    # =====================================================

    config: dict = field(default_factory=dict)

    # =====================================================
    # Informações do Payload
    # =====================================================

    version: str = "1.0"

    generated_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )

    # =====================================================

    def to_dict(self):

        return asdict(self)