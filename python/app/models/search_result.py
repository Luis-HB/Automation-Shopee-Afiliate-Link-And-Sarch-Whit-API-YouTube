from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class SearchResult:

    id: Optional[int] = None

    query_id: Optional[int] = None

    video_id: Optional[int] = None

    position: int = 0

    raw_score: float = 0

    ranking_score: float = 0

    selected: bool = False

    metadata: dict = None

    created_at: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data):

        obj = cls()

        for field in cls.__dataclass_fields__:

            if field in data:

                setattr(obj, field, data[field])

        return obj