from scrapers.promobit.scraper import PromobitScraper
from scrapers.promobit.parser import PromobitParser


scraper = PromobitScraper()

html = scraper.download()

print(html[:500])

parser = PromobitParser()

parser.parse(html)