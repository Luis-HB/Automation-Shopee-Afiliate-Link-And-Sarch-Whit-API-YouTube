from bs4 import BeautifulSoup


class PromobitParser:

    @staticmethod
    def parse(html):

        soup = BeautifulSoup(html, "lxml")

        print(soup.title)

        return soup