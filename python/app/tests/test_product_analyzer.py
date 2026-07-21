from services.product.product_analyzer import ProductAnalyzer

dados = ProductAnalyzer.analisar(
    "Mouse Gamer Logitech G203 Lightsync RGB Preto"
)

print(dados)