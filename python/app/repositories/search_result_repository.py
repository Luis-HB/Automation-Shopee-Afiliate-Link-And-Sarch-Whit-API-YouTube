from repositories.base_repository import Repository
from models.search_result import SearchResult


class SearchResultRepository(Repository):

    def __init__(self):

        super().__init__(
            "search_results",
            SearchResult
        )

    def find_by_query(self, query_id):

        return self.where(
            "query_id",
            query_id
        ).get()

    def find_selected(self):

        return (
            self.where("selected", True)
            .get()
        )