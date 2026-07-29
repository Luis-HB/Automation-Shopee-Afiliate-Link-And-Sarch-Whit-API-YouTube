class AIContextSerializer:

    def serialize(self, context):

        return {

            "produto": self._product(context),

            "consultas": self._queries(context),

            "videos": self._videos(context),

            "metadata": context.metadata

        }

    # =====================================================

    def _product(self, context):

        produto = context.produto

        return {

            "titulo": produto.titulo,

            "descricao": produto.descricao,

            "preco": float(produto.preco),

            "preco_original": float(produto.preco_original),

            "desconto": float(produto.desconto),

            "nota": float(produto.nota),

            "avaliacoes": produto.avaliacoes,

            "vendas": produto.vendas,

            "score": float(produto.score),

            "url_produto": produto.url_produto

        }

    # =====================================================

    def _queries(self, context):

        consultas = []

        for query in context.consultas:

            consultas.append({

                "provider": query.provider,

                "query": query.query,

                "status": query.status,

                "videos_encontrados": query.videos_found

            })

        return consultas

    # =====================================================

    def _videos(self, context):

        videos = []

        for video in context.videos:

            videos.append({

                "titulo": video.titulo,

                "canal": video.canal,

                "views": video.views,

                "likes": video.likes,

                "duracao": video.duracao,

                "score": float(video.score),

                "url": video.url

            })

        return videos