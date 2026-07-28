from models.search_result import SearchResult


class SearchResultFactory:

    @staticmethod
    def create(

        query_id,

        video,

        position,

        raw_score,

        ranking_score,

        selected=False,

        metadata=None

    ):

        result = SearchResult()

        result.query_id = query_id

        result.video_id = video.id

        result.position = position

        result.raw_score = raw_score

        result.ranking_score = ranking_score

        result.selected = selected

        result.metadata = metadata or {}

        return result