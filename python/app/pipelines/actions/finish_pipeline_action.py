import time

from services.status.status_service import StatusService


class FinishPipelineAction:

    def execute(

        self,

        product,

        result,

        start_time,

        videos_saved

    ):

        # ---------------------------------
        # Status
        # ---------------------------------

        if videos_saved > 0:

            StatusService.pronto(product)

            result.success = True

        else:

            StatusService.sem_video(product)

            result.success = False

        # ---------------------------------
        # Tempo
        # ---------------------------------

        elapsed = round(

            time.perf_counter() - start_time,

            2

        )

        result.processing_time = elapsed
        result.pipeline = "affiliate"
        result.version = "4.0"

        result.set_metadata(

            processing_time=elapsed,

            pipeline="affiliate",

            version="4.0",

            videos_saved=videos_saved

        )

        print(f"STATUS FINAL: {product.status}")
        print("=" * 70)

        return result

    # --------------------------
    # Compatibilidade
    # --------------------------

    def process(self, *args, **kwargs):
        return self.execute(*args, **kwargs)

    def executar(self, *args, **kwargs):
        return self.execute(*args, **kwargs)