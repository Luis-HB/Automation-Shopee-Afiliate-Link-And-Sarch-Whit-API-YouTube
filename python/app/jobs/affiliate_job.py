from pipelines.affiliate_pipeline import AffiliatePipeline


class AffiliateJob:

    def __init__(self):

        self.pipeline = AffiliatePipeline()

    def execute(self):

        print("=" * 70)
        print("AFFILIATE JOB")
        print("=" * 70)

        return self.pipeline.execute()