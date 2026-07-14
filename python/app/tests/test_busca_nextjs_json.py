from bs4 import BeautifulSoup

from scrapers.promobit.scraper import PromobitScraper

scraper = PromobitScraper()

html = scraper.download()

soup = BeautifulSoup(html, "lxml")

for script in soup.find_all("script"):

    texto = script.get_text()

    if "__NEXT_DATA__" in texto:

        print(texto[:1000])