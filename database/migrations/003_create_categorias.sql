CREATE TABLE categorias (

    id BIGSERIAL PRIMARY KEY,

    nome VARCHAR(150) NOT NULL UNIQUE,

    slug VARCHAR(150) NOT NULL UNIQUE,

    ativa BOOLEAN DEFAULT TRUE,

    prioridade INTEGER DEFAULT 100,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

INSERT INTO categorias (nome, slug) VALUES
('Celulares','celulares'),
('Informática','informatica'),
('Casa','casa'),
('Moda','moda'),
('Games','games'),
('Áudio','audio'),
('Smart Home','smart-home'),
('TV','tv'),
('Beleza','beleza'),
('Esporte','esporte');