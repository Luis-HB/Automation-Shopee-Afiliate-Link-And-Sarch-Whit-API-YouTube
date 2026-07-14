import requests


class PromobitScraper:

    BASE_URL = "https://www.promobit.com.br/promocoes/loja/shopee/"

    def download(self):

        headers = {

            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/138.0 Safari/537.36"
            )

        }

        response = requests.get(

            self.BASE_URL,

            headers=headers,

            timeout=30

        )

        response.raise_for_status()

        return response.text