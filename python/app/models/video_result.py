from dataclasses import dataclass
from typing import Optional


@dataclass
class VideoResult:

    video_id: str

    titulo: str

    url: str

    thumbnail: str

    canal: str

    views: int = 0

    likes: int = 0

    duracao: int = 0

    score: float = 0

    provider: str = ""

    # =====================================================
    # Origem do vídeo
    # =====================================================

    query: str = ""

    query_order: int = 0

    query_id: Optional[int] = None

    provider_query_id: Optional[int] = None

    # =====================================================

    metadata: dict | None = None