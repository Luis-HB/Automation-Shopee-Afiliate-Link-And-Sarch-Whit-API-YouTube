from dataclasses import dataclass, field
from typing import List, Optional

from models.product import Product
from models.video_result import VideoResult
from models.discovery_result import DiscoveryResult
from models.ranking_result import RankingResult


@dataclass
class PipelineResult:

    product: Product

    videos: List[VideoResult] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)

    discovery: Optional[DiscoveryResult] = None

    ranking: Optional[RankingResult] = None

    errors: List[str] = field(default_factory=list)

    success: bool = True

    processing_time: float = 0

    pipeline: str = "affiliate"

    version: str = "4.0"

    # -----------------------------------------------------

    def add_video(self, video):

        self.videos.append(video)

    # -----------------------------------------------------

    def add_error(self, error):

        self.errors.append(str(error))
        self.success = False

    # -----------------------------------------------------

    # Compatibilidade com o código atual
    def set_metadata(self, **kwargs):

        self.metadata.update(kwargs)

    # -----------------------------------------------------

    @property
    def videos_found(self):

        if self.discovery is not None:
            return self.discovery.total

        return len(self.videos)

    @property
    def videos_ranked(self):

        if self.ranking is not None:
            return self.ranking.total

        return len(self.videos)

    # -----------------------------------------------------

    def to_dict(self):

        return {

            "success": self.success,

            "product": self.product,

            "videos": self.videos,

            "discovery": self.discovery,

            "ranking": self.ranking,

            "metadata": self.metadata,

            "processing_time": self.processing_time,

            "pipeline": self.pipeline,

            "version": self.version,

            "errors": self.errors

        }