from services.search.search_query_builder import SearchQueryBuilder


class BuildQueriesAction:

    def execute(self, product, result):

        print("2 - Queries")

        queries = SearchQueryBuilder.generate(product)

        query_objects = []

        for ordem, query in enumerate(queries, start=1):

            query_objects.append(
                {
                    "provider": "youtube",
                    "ordem": ordem,
                    "query": query
                }
            )

        print()

        for item in query_objects:
            print(
                f"[{item['provider']}] "
                f"{item['ordem']:02d} -> "
                f"{item['query']}"
            )

        result.set_metadata(

            source="affiliate_api",

            queries_generated=len(query_objects),

            search_strategy="multi_provider",

            queries=query_objects

        )

        return query_objects

    # -------------------------------------------------
    # Alias
    # -------------------------------------------------

    def executar(self, product, result):
        return self.execute(product, result)