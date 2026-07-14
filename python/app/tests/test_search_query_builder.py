from services.search_query_builder import SearchQueryBuilder
from models.produto import Produto

produto = Produto(
    titulo="Mouse Logitech G203 Lightsync RGB"
)

for consulta in SearchQueryBuilder.gerar(produto):
    print(consulta)