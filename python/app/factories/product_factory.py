import hashlib
from decimal import Decimal

from models.product import Product


class ProductFactory:

    @staticmethod
    def from_dict(data):

        url = (
            data.get("shopee_url")
            or data.get("url_shopee")
            or data.get("product_url")
            or data.get("url_produto")
            or data.get("title")
            or data.get("titulo", "")
        )

        hash_produto = hashlib.sha256(
            url.encode("utf-8")
        ).hexdigest()

        return Product(

            hash_produto=hash_produto,

            titulo=data.get("title") or data.get("titulo", ""),

            descricao=data.get("description") or data.get("descricao"),

            preco=Decimal(str(data.get("price") or data.get("preco", 0))),

            preco_original=Decimal(
                str(data.get("original_price") or data.get("preco_original", 0))
            ),

            desconto=Decimal(
                str(data.get("discount") or data.get("desconto", 0))
            ),

            nota=data.get("rating") or data.get("nota"),

            avaliacoes=data.get("reviews") or data.get("avaliacoes"),

            vendas=data.get("sales") or data.get("vendas"),

            estoque=data.get("stock") or data.get("estoque"),

            imagem_principal=data.get("image") or data.get("imagem", ""),

            url_produto=data.get("product_url") or data.get("url_produto", ""),

            url_afiliado=data.get("shopee_url") or data.get("url_shopee", ""),

            score=Decimal(str(data.get("score", 0))),

            status="NOVO",

            ativo=True

        )

    @staticmethod
    def from_affiliate_api(data):

        url = (
            data.get("offerLink")
            or data.get("productLink")
            or str(data.get("itemId", ""))
        )

        hash_produto = hashlib.sha256(
            url.encode("utf-8")
        ).hexdigest()

        return Product(

            shopee_id=str(data.get("itemId", "")),

            hash_produto=hash_produto,

            titulo=data.get("productName", ""),

            preco=Decimal(str(data.get("priceMin", 0))),

            preco_original=Decimal(
                str(data.get("priceMax", 0))
            ),

            desconto=Decimal(
                str(data.get("priceDiscountRate", 0))
            ),

            nota=Decimal(
                str(data.get("ratingStar", 0))
            ),

            avaliacoes=data.get("ratingCount"),

            vendas=data.get("sales"),

            imagem_principal=data.get("imageUrl", ""),

            url_produto=data.get("productLink", ""),

            url_afiliado=data.get("offerLink", ""),

            score=Decimal("0"),

            status="NOVO",

            ativo=True,

            api_response=data

        )