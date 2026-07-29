from models.product_context import ProductContext


class ContextBuilderService:

    def build(self, context: ProductContext):

        context.metadata = {

            "produto_id": context.produto.id,

            "titulo": context.produto.titulo,

            "status": context.produto.status,

            "consultas": len(context.consultas),

            "videos": len(context.videos),

            "resultados": len(context.resultados)

        }

        return context