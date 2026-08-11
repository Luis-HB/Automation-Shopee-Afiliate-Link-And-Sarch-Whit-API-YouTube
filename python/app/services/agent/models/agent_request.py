from dataclasses import dataclass, field, asdict
from datetime import datetime
from uuid import uuid4


@dataclass
class AgentRequest:

    agent: str = ""

    correlation_id: str = field(
        default_factory=lambda: str(uuid4())
    )

    timestamp: str = field(
        default_factory=lambda: datetime.now(datetime.timezone.utc).isoformat()
    )

    payload: dict = field(default_factory=dict)

    def to_dict(self):

        return asdict(self)