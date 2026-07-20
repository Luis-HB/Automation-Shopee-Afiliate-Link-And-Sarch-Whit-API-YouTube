from python.app.services.search.search_query_builder import SearchQueryBuilder
from python.app.models.product import Produto

produto = Produto(
    titulo="Mouse Logitech G203 Lightsync RGB"
)

for consulta in SearchQueryBuilder.gerar(produto):
    print(consulta)