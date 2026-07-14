from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Video:

    id: Optional[int] = None

    produto_id: Optional[int] = None

    youtube_id: str = ""

    titulo: str = ""

    canal: str = ""

    thumbnail: str = ""

    url: str = ""

    views: int = 0

    likes: int = 0

    duracao: int = 0

    score: float = 0

    created_at: Optional[datetime] = None