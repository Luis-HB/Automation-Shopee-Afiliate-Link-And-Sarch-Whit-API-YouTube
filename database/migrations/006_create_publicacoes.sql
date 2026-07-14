CREATE TABLE publicacoes (

    id BIGSERIAL PRIMARY KEY,

    produto_id BIGINT NOT NULL REFERENCES produtos(id),

    video_id BIGINT NOT NULL REFERENCES videos_produto(id),

    status VARCHAR(20) NOT NULL DEFAULT 'PENDENTE',

    score NUMERIC(8,2),

    legenda TEXT,

    hashtags TEXT,

    data_agendada TIMESTAMP,

    publicado_em TIMESTAMP,

    created_at TIMESTAMP DEFAULT NOW(),

    updated_at TIMESTAMP DEFAULT NOW()
);