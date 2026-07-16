import hashlib

from decimal import Decimal

from models.produto import Produto


class ProdutoFactory:

    @staticmethod
    def from_dict(data):

        url = (
            data.get("url_shopee")
            or data.get("url_produto")
            or data.get("titulo", "")
        )

        hash_produto = hashlib.sha256(
            url.encode("utf-8")
        ).hexdigest()

        return Produto(

            hash_produto=hash_produto,

            titulo=data.get("titulo", ""),

            descricao=data.get("descricao"),

            preco=Decimal(str(data.get("preco", 0))),

            preco_original=Decimal(str(data.get("preco_original", 0))),

            desconto=Decimal(str(data.get("desconto", 0))),

            nota=data.get("nota"),

            avaliacoes=data.get("avaliacoes"),

            vendas=data.get("vendas"),

            estoque=data.get("estoque"),

            imagem_principal=data.get("imagem", ""),

            url_produto=data.get("url_produto", ""),

            url_afiliado=data.get("url_shopee", ""),

            score=Decimal(str(data.get("score", 0))),

            status="NOVO",

            ativo=True

        )
        
    @staticmethod
    def from_affiliate_api(data):

        return Produto(

        shopee_id=data["itemId"],

        titulo=data["productName"],

        preco=data["priceMin"],

        preco_original=data["priceMax"],

        desconto=data["priceDiscountRate"],

        nota=data["ratingStar"],

        vendas=data["sales"],

        imagem_principal=data["imageUrl"],

        url_produto=data["productLink"],

        url_afiliado=data["offerLink"],

        api_response=data
    )