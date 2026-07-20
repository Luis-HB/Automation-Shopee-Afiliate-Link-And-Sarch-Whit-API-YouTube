from python.app.services.affiliate.affiliate_service import AffiliateService

api = AffiliateService()

produtos = api.buscar_produtos(

    keyword="Mouse Logitech G203",

    limit=5

)

for produto in produtos:

    print("-" * 80)

    print(produto["productName"])

    print(produto["commissionRate"])

    print(produto["priceMin"])

    print(produto["sales"])