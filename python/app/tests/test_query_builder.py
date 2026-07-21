from repositories.product_repository import ProductRepository

repo = ProductRepository()

print("\nProdutos NOVOS:\n")

produtos = repo.listar_novos()

for produto in produtos:
    print(produto)

print("\nBuscar por hash:\n")

produto = repo.buscar_por_hash("123456789")

print(produto)

repo.close()