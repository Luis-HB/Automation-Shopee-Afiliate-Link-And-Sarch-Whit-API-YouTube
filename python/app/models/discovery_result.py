from dataclasses import dataclass, field
from typing import List

from models.video_result import VideoResult
from models.query_result import QueryResult


@dataclass
class DiscoveryResult:

    # --------------------------------------------------
    # Compatibilidade
    # --------------------------------------------------

    videos: List[VideoResult] = field(default_factory=list)

    # --------------------------------------------------
    # Novo
    # --------------------------------------------------

    queries: List[QueryResult] = field(default_factory=list)

    providers: List[str] = field(default_factory=list)

    failed_providers: List[str] = field(default_factory=list)

    elapsed: float = 0.0

    quota_exceeded: bool = False

    # --------------------------------------------------

    @property
    def total(self):

        return len(self.videos)

    @property
    def success(self):

        return not self.quota_exceeded

    @property
    def queries_total(self):

        return len(self.queries)

    # --------------------------------------------------

    def add_provider(self, name):

        if name not in self.providers:
            self.providers.append(name)

    def add_failed_provider(self, name):

        if name not in self.failed_providers:
            self.failed_providers.append(name)

    # --------------------------------------------------

    def add_video(self, video):

        self.videos.append(video)

    def extend(self, videos):

        self.videos.extend(videos)

    # --------------------------------------------------
    # Novo
    # --------------------------------------------------

    def add_query(self, query):

        self.queries.append(query)