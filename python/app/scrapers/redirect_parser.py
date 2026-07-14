import re
import requests


class RedirectParser:

    @staticmethod
    def get_shopee_link(url):

        html = requests.get(url).text

        match = re.search(
            r"https://s\.shopee\.com\.br/[A-Za-z0-9?=&/_-]+",
            html
        )

        if match:
            return match.group(0)

        return None