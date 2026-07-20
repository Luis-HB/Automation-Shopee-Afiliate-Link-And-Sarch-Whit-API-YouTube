import hashlib
import hmac


class ShopeeSigner:
    """
    Utilitário para geração de assinatura HMAC-SHA256.

    Atualmente não é utilizado pela Affiliate GraphQL API,
    mas pode ser usado futuramente na Partner API.
    """

    @staticmethod
    def sign(base_string: str, partner_key: str) -> str:

        return hmac.new(
            partner_key.encode("utf-8"),
            base_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()