from scrapers.promobit.crawler import PromobitCrawler

crawler = PromobitCrawler()

links = crawler.listar_ofertas()

print(f"Foram encontradas {len(links)} ofertas\n")

for link in links[:10]:

    print(link)