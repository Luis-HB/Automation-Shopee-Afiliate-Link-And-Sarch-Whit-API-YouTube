from dataclasses import dataclass, field
from typing import List

from models.video_result import VideoResult


@dataclass
class RankingResult:

    videos: List[VideoResult] = field(default_factory=list)

    discarded: int = 0

    elapsed: float = 0

    average_score: float = 0

    highest_score: float = 0

    lowest_score: float = 0

    @property
    def total(self):

        return len(self.videos)

    @property
    def approved(self):

        return len(self.videos)

    def add(self, video):

        self.videos.append(video)

    def calculate_statistics(self):

        if not self.videos:
            return

        scores = [v.score for v in self.videos]

        self.average_score = round(
            sum(scores) / len(scores),
            2
        )

        self.highest_score = max(scores)

        self.lowest_score = min(scores)