import hashlib


class ProductHashService:

    @staticmethod
    def generate(value: str) -> str:

        if value is None:
            value = ""

        return hashlib.sha256(
            value.encode("utf-8")
        ).hexdigest()