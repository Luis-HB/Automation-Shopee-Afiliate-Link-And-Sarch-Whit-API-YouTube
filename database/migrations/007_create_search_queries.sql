CREATE TABLE search_queries (

    id                  BIGSERIAL PRIMARY KEY,

    produto_id          BIGINT NOT NULL,

    provider            VARCHAR(50) NOT NULL,

    query               TEXT NOT NULL,

    ordem               INTEGER NOT NULL DEFAULT 1,

    status              VARCHAR(20) NOT NULL DEFAULT 'PENDING',

    videos_found        INTEGER NOT NULL DEFAULT 0,

    elapsed_ms          INTEGER NOT NULL DEFAULT 0,

    created_at          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_search_query_produto
        FOREIGN KEY (produto_id)
        REFERENCES produtos(id)
        ON DELETE CASCADE,

    CONSTRAINT chk_search_query_provider
        CHECK (
            provider IN (
                'youtube',
                'tiktok',
                'instagram',
                'shopee'
            )
        ),

    CONSTRAINT chk_search_query_status
        CHECK (
            status IN (
                'PENDING',
                'SUCCESS',
                'EMPTY',
                'FAILED'
            )
        )

);

CREATE INDEX idx_search_queries_produto
ON search_queries(produto_id);

CREATE INDEX idx_search_queries_provider
ON search_queries(provider);

CREATE INDEX idx_search_queries_status
ON search_queries(status);

CREATE INDEX idx_search_queries_created
ON search_queries(created_at);