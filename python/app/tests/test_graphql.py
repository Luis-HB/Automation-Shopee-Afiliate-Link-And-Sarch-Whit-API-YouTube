from python.app.services.affiliate.affiliate_service import AffiliateService

api = AffiliateService()

produtos = api.buscar_produtos(
    keyword="mouse gamer",
    page=1,
    limit=3
)

print(produtos)