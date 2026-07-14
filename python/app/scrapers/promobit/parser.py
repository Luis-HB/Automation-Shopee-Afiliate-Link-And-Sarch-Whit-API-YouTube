from bs4 import BeautifulSoup


class PromobitParser:

    def parse(self, html):

        soup = BeautifulSoup(html, "lxml")

        print(soup.title)

        return soup