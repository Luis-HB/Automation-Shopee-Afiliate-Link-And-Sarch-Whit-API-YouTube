from bs4 import BeautifulSoup

from scrapers.promobit.scraper import PromobitScraper

scraper = PromobitScraper()

html = scraper.download()

soup = BeautifulSoup(html, "lxml")

print("=" * 80)

for link in soup.find_all("a", href=True):

    href = link["href"]

    if "/oferta/" in href:

        print(href)