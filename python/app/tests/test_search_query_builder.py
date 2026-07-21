from services.search.search_query_builder import SearchQueryBuilder
from models.product import Product

produto = Product(
    titulo="Mouse Logitech G203 Lightsync RGB"
)

for consulta in SearchQueryBuilder.gerar(produto):
    print(consulta)