from dataclasses import dataclass, field


@dataclass
class AgentResponse:

    decision: str = "REJECT"

    confidence: float = 0.0

    score: float = 0.0

    reason: str = ""

    recommendations: list = field(
        default_factory=list
    )

    commercial_analysis: dict = field(
        default_factory=dict
    )

    metadata: dict = field(
        default_factory=dict
    )