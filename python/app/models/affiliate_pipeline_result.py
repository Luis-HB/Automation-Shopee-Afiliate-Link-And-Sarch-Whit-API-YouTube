from dataclasses import dataclass, field
from typing import List

from models.pipeline_result import PipelineResult


@dataclass
class AffiliatePipelineResult:

    pipeline_results: List[PipelineResult] = field(default_factory=list)

    products_found: int = 0

    products_processed: int = 0

    products_failed: int = 0

    pages_processed: int = 0

    processing_time: float = 0

    success: bool = True

    errors: List[str] = field(default_factory=list)

    # -----------------------------------------------------

    def add_result(self, result):

        self.pipeline_results.append(result)

        self.products_processed += 1

        if not result.success:

            self.products_failed += 1

    # -----------------------------------------------------

    def add_error(self, error):

        self.errors.append(str(error))

        self.success = False

    # -----------------------------------------------------

    @property
    def videos_found(self):

        total = 0

        for result in self.pipeline_results:

            total += result.videos_found

        return total

    @property
    def videos_saved(self):

        total = 0

        for result in self.pipeline_results:

            total += len(result.videos)

        return total