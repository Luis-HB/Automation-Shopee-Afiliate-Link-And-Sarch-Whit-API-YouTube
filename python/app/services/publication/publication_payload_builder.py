from datetime import datetime


class PublicationPayloadBuilder:

    @staticmethod
    def build(product, video):

        return {

            "product": {

                "id": product.id,
                "title": product.titulo,
                "description": product.descricao,
                "price": float(product.preco or 0),
                "original_price": float(product.preco_original or 0),
                "discount": float(product.desconto or 0),
                "affiliate_url": product.url_afiliado,
                "product_url": product.url_produto,
                "image": product.imagem_principal,
                "score": float(product.score or 0),
                "status": product.status,

            },

            "video": {

                "id": video.id,
                "youtube_id": video.youtube_id,
                "title": video.titulo,
                "channel": video.canal,
                "thumbnail": video.thumbnail,
                "url": video.url,
                "views": video.views,
                "likes": video.likes,
                "duration": video.duracao,
                "score": video.score,

            },

            "metadata": {

                "generated_at": datetime.utcnow().isoformat(),
                "pipeline": "publication",

            }

        }