from bs4 import BeautifulSoup

from scrapers.promobit.scraper import PromobitScraper


scraper = PromobitScraper()

html = scraper.download()

soup = BeautifulSoup(html, "lxml")

print("=" * 80)
print("TÍTULO")
print("=" * 80)
print(soup.title.text)

print("\n")

print("=" * 80)
print("PRIMEIRAS DIVS COM CLASSE")
print("=" * 80)

classes = set()

for tag in soup.find_all(True):

    if tag.get("class"):

        classes.add(" ".join(tag["class"]))

for classe in sorted(classes):

    print(classe)