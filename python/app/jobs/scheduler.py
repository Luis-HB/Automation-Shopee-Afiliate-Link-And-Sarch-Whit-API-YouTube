from jobs.affiliate_job import AffiliateJob
from jobs.publication_job import PublicationJob


class Scheduler:

    def run(self):

        print("=" * 70)
        print("INICIANDO SCHEDULER")
        print("=" * 70)

        try:

            AffiliateJob().execute()

        except Exception as e:

            print(f"[AffiliateJob] {e}")

        try:

            PublicationJob().execute()

        except Exception as e:

            if "429" in str(e):
                raise RuntimeError("Quota da API do YouTube excedida")

            raise