from dataclasses import dataclass, field
from typing import List

from models.video_result import VideoResult


@dataclass
class DiscoveryResult:

    videos: List[VideoResult] = field(default_factory=list)

    providers: List[str] = field(default_factory=list)

    failed_providers: List[str] = field(default_factory=list)

    elapsed: float = 0.0

    quota_exceeded: bool = False

    @property
    def total(self) -> int:
        return len(self.videos)

    @property
    def success(self) -> bool:
        return not self.quota_exceeded

    def add_provider(self, name: str):

        if name not in self.providers:
            self.providers.append(name)

    def add_failed_provider(self, name: str):

        if name not in self.failed_providers:
            self.failed_providers.append(name)

    def add_video(self, video: VideoResult):

        self.videos.append(video)

    def extend(self, videos: List[VideoResult]):

        self.videos.extend(videos)