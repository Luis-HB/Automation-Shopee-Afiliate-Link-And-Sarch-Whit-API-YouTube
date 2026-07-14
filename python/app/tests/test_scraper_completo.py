from scrapers.promobit_scraper import PromobitScraper

scraper = PromobitScraper()

produtos = scraper.executar(3)

print("=" * 80)

for produto in produtos:

    print("ID:", produto.id)
    print("Título:", produto.titulo)
    print("Preço:", produto.preco)
    print("Hash:", produto.hash_produto)
    print("Imagem:", produto.imagem_principal)
    print("Shopee:", produto.url_produto)
    print("Afiliado:", produto.url_afiliado)
    print("Status:", produto.status)

    print("=" * 80)