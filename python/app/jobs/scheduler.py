from jobs.affiliate_job import AffiliateJob
from jobs.publication_job import PublicationJob


class Scheduler:

    def run(self):

        print("=" * 70)
        print("INICIANDO SCHEDULER")
        print("=" * 70)

        affiliate_result = None

        # -----------------------------------
        # Affiliate
        # -----------------------------------

        try:

            affiliate_result = AffiliateJob().execute()

        except Exception as e:

            print(f"[AffiliateJob] {e}")

        # -----------------------------------
        # Publication
        # -----------------------------------

        try:

            PublicationJob().execute()

        except Exception as e:

            print(f"[PublicationJob] {e}")

        return affiliate_result