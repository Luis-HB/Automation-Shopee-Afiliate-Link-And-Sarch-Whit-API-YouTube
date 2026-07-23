CREATE TABLE produtos (

    id BIGSERIAL PRIMARY KEY,

    descoberta_id BIGINT,

    shopee_id VARCHAR(100),

    hash_produto VARCHAR(64) UNIQUE NOT NULL,

    titulo TEXT NOT NULL,

    descricao TEXT,

    categoria_id BIGINT,

    preco NUMERIC(10,2),

    preco_original NUMERIC(10,2),

    desconto NUMERIC(5,2),

    nota NUMERIC(3,2),

    avaliacoes INTEGER,

    vendas INTEGER,

    estoque INTEGER,

    imagem_principal TEXT,

    url_produto TEXT,

    url_afiliado TEXT,

    score NUMERIC(5,2) DEFAULT 0,

    status VARCHAR(30) DEFAULT 'NOVO',

    ativo BOOLEAN DEFAULT TRUE,

    ultima_verificacao TIMESTAMP,

    api_response JSONB,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    status_updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_descoberta
        FOREIGN KEY (descoberta_id)
        REFERENCES descoberta_produtos(id)

);

CREATE INDEX idx_produtos_status
ON produtos(status);

CREATE INDEX idx_produtos_score
ON produtos(score DESC);

CREATE INDEX idx_produtos_categoria
ON produtos(categoria_id);

CREATE INDEX idx_produtos_hash
ON produtos(hash_produto);