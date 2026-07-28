from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class SearchQuery:

    id: Optional[int] = None

    produto_id: Optional[int] = None

    provider: str = ""

    query: str = ""

    ordem: int = 1

    status: str = "PENDING"

    videos_found: int = 0

    elapsed_ms: int = 0

    created_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data):

        obj = cls()

        for field in cls.__dataclass_fields__:

            if field in data:
                setattr(obj, field, data[field])

        return obj