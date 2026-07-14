from dataclasses import dataclass
from datetime import datetime


@dataclass
class Publicacao:

    id: int | None = None

    produto_id: int = None
    video_id: int = None

    status: str = "PENDENTE"

    score: float = 0

    legenda: str = ""

    hashtags: str = ""

    data_agendada: datetime | None = None

    publicado_em: datetime | None = None

    created_at: datetime | None = None
    updated_at: datetime | None = None