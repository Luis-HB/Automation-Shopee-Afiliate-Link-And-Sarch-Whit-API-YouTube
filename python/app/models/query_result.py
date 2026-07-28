from dataclasses import dataclass, field
from typing import List

from models.video_result import VideoResult


@dataclass
class QueryResult:

    provider: str

    query: str

    ordem: int

    elapsed: float = 0

    videos: List[VideoResult] = field(default_factory=list)

    @property
    def total(self):

        return len(self.videos)

    @property
    def success(self):

        return self.total > 0