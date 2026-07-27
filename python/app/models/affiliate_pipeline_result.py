from dataclasses import dataclass, field
from typing import List

from models.pipeline_result import PipelineResult


@dataclass
class AffiliatePipelineResult:

    results: List[PipelineResult] = field(default_factory=list)

    errors: List[str] = field(default_factory=list)

    processing_time: float = 0

    pages_processed: int = 0

    def add_result(self, result: PipelineResult):

        self.results.append(result)

    def add_error(self, error):

        self.errors.append(str(error))

    # -------------------------------------------------
    # Estatísticas calculadas automaticamente
    # -------------------------------------------------

    @property
    def products_found(self):
        return len(self.results)

    @property
    def products_processed(self):
        return len(self.results)

    @property
    def products_failed(self):
        return len([r for r in self.results if not r.success])

    @property
    def videos_found(self):
        return sum(
            getattr(r.discovery, "total", 0)
            for r in self.results
            if r.discovery
        )

    @property
    def videos_ranked(self):
        return sum(
            getattr(r.ranking, "total", 0)
            for r in self.results
            if r.ranking
        )

    @property
    def videos_saved(self):
        return sum(
            len(r.videos)
            for r in self.results
        )

    @property
    def success(self):
        return self.products_failed == 0

    def to_dict(self):

        return {
            "success": self.success,
            "pages_processed": self.pages_processed,
            "products_found": self.products_found,
            "products_processed": self.products_processed,
            "products_failed": self.products_failed,
            "videos_found": self.videos_found,
            "videos_ranked": self.videos_ranked,
            "videos_saved": self.videos_saved,
            "processing_time": self.processing_time,
            "errors": self.errors,
            "results": self.results
        }