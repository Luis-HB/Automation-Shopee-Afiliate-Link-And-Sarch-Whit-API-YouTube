from models.search_query import SearchQuery


class SearchQueryFactory:

    @staticmethod
    def create(
        produto_id: int,
        provider: str,
        query: str,
        ordem: int
    ) -> SearchQuery:

        search_query = SearchQuery()

        search_query.produto_id = produto_id
        search_query.provider = provider
        search_query.query = query
        search_query.ordem = ordem

        search_query.status = "PENDING"
        search_query.videos_found = 0
        search_query.elapsed_ms = 0

        return search_query

    # -------------------------------------------------------
    # Compatibilidade
    # -------------------------------------------------------

    @staticmethod
    def from_dict(data):

        return SearchQuery.from_dict(data)