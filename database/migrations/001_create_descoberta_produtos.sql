CREATE TABLE descoberta_produtos (

    id BIGSERIAL PRIMARY KEY,

    origem VARCHAR(50) NOT NULL,

    origem_id VARCHAR(200),

    hash_produto VARCHAR(64) UNIQUE NOT NULL,

    titulo TEXT NOT NULL,

    preco NUMERIC(10,2),

    preco_original NUMERIC(10,2),

    desconto NUMERIC(5,2),

    imagem_principal TEXT,

    url_promobit TEXT,

    url_shopee TEXT,

    categoria VARCHAR(150),

    loja VARCHAR(100),

    status VARCHAR(30) DEFAULT 'DESCOBERTO',

    api_response JSONB,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE INDEX idx_descoberta_hash
ON descoberta_produtos(hash_produto);

CREATE INDEX idx_descoberta_status
ON descoberta_produtos(status);

CREATE INDEX idx_descoberta_origem
ON descoberta_produtos(origem);

CREATE INDEX idx_descoberta_created
ON descoberta_produtos(created_at DESC);