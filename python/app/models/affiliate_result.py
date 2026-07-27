from dataclasses import dataclass, field
from typing import List

from models.pipeline_result import PipelineResult


@dataclass
class AffiliateResult:

    pipelines: List[PipelineResult] = field(default_factory=list)

    pages_processed: int = 0

    products_found: int = 0

    products_processed: int = 0

    products_failed: int = 0

    success: bool = True

    def add_pipeline(self, pipeline: PipelineResult):

        self.pipelines.append(pipeline)

        self.products_processed += 1

        if not pipeline.success:
            self.products_failed += 1

    def add_failure(self):

        self.products_failed += 1

        self.success = False

    @property
    def total(self):

        return len(self.pipelines)