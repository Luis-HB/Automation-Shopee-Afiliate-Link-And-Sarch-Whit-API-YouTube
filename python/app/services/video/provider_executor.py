from services.video.provider_health_manager import (
    ProviderHealthManager
)


class ProviderExecutor:

    @staticmethod
    def execute(provider, queries):

        if not ProviderHealthManager.is_enabled(
            provider.name
        ):
            return []

        try:

            return provider.search(queries)

        except RuntimeError as e:

            if str(e) == "YOUTUBE_QUOTA_EXCEEDED":

                ProviderHealthManager.disable(
                    provider.name,
                    "quota_exceeded"
                )

                print()
                print("=" * 70)
                print(
                    f"{provider.name.upper()} DESABILITADO"
                )
                print("Motivo: quota_exceeded")
                print("=" * 70)
                print()

                return []

            raise

        except Exception as e:

            ProviderHealthManager.disable(
                provider.name,
                str(e)
            )

            print()
            print("=" * 70)
            print(
                f"{provider.name.upper()} DESABILITADO"
            )
            print(e)
            print("=" * 70)
            print()

            return []