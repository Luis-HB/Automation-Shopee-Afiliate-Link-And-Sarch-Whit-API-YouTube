from pipelines.affiliate_pipeline import AffiliatePipeline


class AffiliateJob:

    def __init__(self):

        self.pipeline = AffiliatePipeline()

    def execute(self):

        print("=" * 70)
        print("AFFILIATE JOB")
        print("=" * 70)

        try:

            return self.pipeline.execute()

        except RuntimeError as e:

            if str(e) == "YOUTUBE_QUOTA_EXCEEDED":

                print()
                print("=" * 70)
                print("Quota da API do YouTube esgotada.")
                print("AffiliateJob interrompido.")
                print("=" * 70)
                print()

                raise

            raise