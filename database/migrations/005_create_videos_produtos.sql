CREATE TABLE videos_produto (

    id BIGSERIAL PRIMARY KEY,

    produto_id BIGINT NOT NULL,

    youtube_id VARCHAR(30) NOT NULL,

    titulo TEXT,

    canal TEXT,

    thumbnail TEXT,

    url TEXT,

    views BIGINT,

    likes BIGINT,

    duracao INTEGER,

    score NUMERIC(10,2) DEFAULT 0,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_produto
        FOREIGN KEY (produto_id)
        REFERENCES produtos(id),

    CONSTRAINT uk_video
        UNIQUE (youtube_id)
);