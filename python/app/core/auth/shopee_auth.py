import hashlib
import json
import time


class ShopeeAuth:

    def __init__(self, app_id, secret):

        if not app_id:
            raise ValueError("SHOPEE_APP_ID não configurado.")

        if not secret:
            raise ValueError("SHOPEE_SECRET não configurado.")

        self.app_id = str(app_id)
        self.secret = secret

    def _generate_signature(self, payload, timestamp):

        message = (
            self.app_id +
            timestamp +
            payload +
            self.secret
        )

        return hashlib.sha256(
            message.encode("utf-8")
        ).hexdigest()

    def build_headers(self, body):

        payload = json.dumps(
            body,
            separators=(",", ":"),
            ensure_ascii=False
        )

        timestamp = str(int(time.time()))

        signature = self._generate_signature(
            payload,
            timestamp
        )

        return {

            "Authorization": (
                f"SHA256 Credential={self.app_id}, "
                f"Timestamp={timestamp}, "
                f"Signature={signature}"
            ),

            "Content-Type": "application/json",
            "Accept": "application/json"

        }