import hashlib
import hmac


class ShopeeSigner:

    @staticmethod
    def sign(base_string, partner_key):

        return hmac.new(
            partner_key.encode(),
            base_string.encode(),
            hashlib.sha256
        ).hexdigest()