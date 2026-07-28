CREATE TABLE search_results (

    id BIGSERIAL PRIMARY KEY,

    query_id BIGINT NOT NULL,

    video_id BIGINT NOT NULL,

    position INTEGER NOT NULL,

    raw_score NUMERIC(8,4),

    ranking_score NUMERIC(8,4),

    selected BOOLEAN DEFAULT FALSE,

    metadata JSONB,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_search_result_query
        FOREIGN KEY (query_id)
        REFERENCES search_queries(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_search_result_video
        FOREIGN KEY (video_id)
        REFERENCES videos_produto(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_search_results_query
ON search_results(query_id);

CREATE INDEX idx_search_results_video
ON search_results(video_id);

CREATE INDEX idx_search_results_selected
ON search_results(selected);