from repositories.search_query_repository import SearchQueryRepository
from factories.search_query_factory import SearchQueryFactory


class SearchQueryService:

    def __init__(self):

        self.repo = SearchQueryRepository()

    # =====================================================
    # Criação
    # =====================================================

    def start(
        self,
        produto_id: int,
        provider: str,
        query: str,
        ordem: int
    ):

        search_query = SearchQueryFactory.create(
            produto_id=produto_id,
            provider=provider,
            query=query,
            ordem=ordem
        )

        return self.repo.save(search_query)

    # =====================================================
    # Atualizações
    # =====================================================

    def success(
        self,
        search_query,
        videos_found: int,
        elapsed_ms: int
    ):

        search_query.status = "SUCCESS"
        search_query.videos_found = videos_found
        search_query.elapsed_ms = elapsed_ms

        return self.repo.update(search_query)

    def empty(
        self,
        search_query,
        elapsed_ms: int
    ):

        search_query.status = "EMPTY"
        search_query.videos_found = 0
        search_query.elapsed_ms = elapsed_ms

        return self.repo.update(search_query)

    def fail(
        self,
        search_query,
        elapsed_ms: int = 0
    ):

        search_query.status = "FAILED"
        search_query.elapsed_ms = elapsed_ms

        return self.repo.update(search_query)

    # =====================================================
    # Consultas
    # =====================================================

    def find_by_produto(self, produto_id):

        return self.repo.find_by_produto(produto_id)

    def find_by_provider(self, provider):

        return self.repo.find_by_provider(provider)

    def find_by_status(self, status):

        return self.repo.find_by_status(status)

    # =====================================================
    # Compatibilidade
    # =====================================================

    def iniciar(self, *args, **kwargs):
        return self.start(*args, **kwargs)

    def sucesso(self, *args, **kwargs):
        return self.success(*args, **kwargs)

    def vazio(self, *args, **kwargs):
        return self.empty(*args, **kwargs)

    def falha(self, *args, **kwargs):
        return self.fail(*args, **kwargs)

    def buscar_por_produto(self, produto_id):
        return self.find_by_produto(produto_id)