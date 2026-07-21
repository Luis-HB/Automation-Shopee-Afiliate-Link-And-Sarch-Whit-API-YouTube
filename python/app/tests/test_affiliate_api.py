from services.affiliate.affiliate_service import AffiliateService
from models.search_config import SearchConfig

api = AffiliateService()

config = SearchConfig(
    keyword="mouse gamer",
    page=1,
    limit=10,
    list_type=2,
    sort_type=5
)

produtos = api.buscar_produtos(config)

print(f"{len(produtos)} produtos encontrados")

for produto in produtos[:5]:
    print(produto["productName"])