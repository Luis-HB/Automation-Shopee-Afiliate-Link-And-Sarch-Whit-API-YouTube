from dataclasses import dataclass
from datetime import datetime
from typing import Optional


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

    @classmethod
    def from_dict(cls, data):

        obj = cls()

        for field in cls.__dataclass_fields__:

            if field in data:
                setattr(obj, field, data[field])

        return obj