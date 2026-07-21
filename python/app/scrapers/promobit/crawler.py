from bs4 import BeautifulSoup

from scrapers.promobit.scraper import PromobitScraper


class PromobitCrawler:

    def __init__(self):

        self.scraper = PromobitScraper()

    def listar_ofertas(self):

        html = self.scraper.download()

        soup = BeautifulSoup(html, "lxml")

        links = []

        for a in soup.find_all("a", href=True):

            href = a["href"]

            if "/oferta/" in href:

                if href.startswith("/"):
                    href = "https://www.promobit.com.br" + href

                links.append(href)

        return list(dict.fromkeys(links))