from decimal import Decimal
import uuid

from models.product import Product
from repositories.product_repository import ProductRepository
from services.status.status_service import StatusService


repo = ProductRepository()

# --------------------------------------------------
# Cria um produto temporário
# --------------------------------------------------

produto = Product(
    hash_produto=str(uuid.uuid4()),
    titulo="Produto Teste Status",
    preco=Decimal("99.90"),
    status=StatusService.NOVO,
)

repo.upsert(produto)

print("=" * 60)
print("Produto criado")
print(produto.id, produto.status)

# --------------------------------------------------
# Todos os status
# --------------------------------------------------

transicoes = [
    StatusService.processando,
    StatusService.sem_link,
    StatusService.buscando_videos,
    StatusService.sem_video,
    StatusService.videos_encontrados,
    StatusService.ranqueado,
    StatusService.pronto,
    StatusService.publicado,
    StatusService.expirado,
    StatusService.erro,
]

for func in transicoes:

    func(produto)

    atualizado = repo.find_by("id", produto.id)

    print(
        f"{func.__name__:25} -> {atualizado.status}"
    )

print("=" * 60)

repo.delete(produto.id)

print("Produto removido.")