import hashlib
import json
import time


class ShopeeAuth:

    def __init__(self, app_id, secret):

        if not app_id:
            raise ValueError(
                "SHOPEE_APP_ID não configurado."
            )

        if not secret:
            raise ValueError(
                "SHOPEE_SECRET não configurado."
            )

        self.app_id = str(app_id)
        self.secret = secret
        
    def build_headers(self, body):

        """
        body = dict enviado ao GraphQL
        """

        payload = json.dumps(

            body,

            separators=(",", ":"),

            ensure_ascii=False

        )

        timestamp = str(int(time.time()))

        signature = hashlib.sha256(

            (
                self.app_id +
                timestamp +
                payload +
                self.secret

            ).encode("utf-8")

        ).hexdigest()

        headers = {

            "Authorization":

                f"SHA256 Credential={self.app_id}, "
                f"Timestamp={timestamp}, "
                f"Signature={signature}",

            "Content-Type": "application/json"

        }

        return headers