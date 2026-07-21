import requests


class PromobitScraper:

    BASE_URL = "https://www.promobit.com.br/promocoes/loja/shopee/"

    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0 Safari/537.36"
        )
    }

    def download(self):

        response = requests.get(
            self.BASE_URL,
            headers=self.HEADERS,
            timeout=30
        )

        response.raise_for_status()

        return response.text