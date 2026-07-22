# Shopee & Affiliate Automation Engine

> **Pipeline automatizado em Python para mineração de ofertas, enriquecimento de contexto com vídeo-reviews e ranqueamento inteligente para marketing de afiliados.**

---

## Visão Geral

O **Shopee Affiliate Engine** é uma solução backend desenvolvida para automatizar a jornada de curadoria de conteúdo para afiliados de e-commerce. 

O sistema realiza a raspagem de ofertas em tempo real, valida/desencurta links de afiliados, consulta a API do YouTube em busca de vídeos de *unboxing/review* relevantes para o produto, aplica um algoritmo próprio de **Scoring de Relevância** e disponibiliza um objeto de contexto unificado para consumo por ferramentas de automação (como n8n).

---

## Tecnologias & Arquitetura

* **Linguagem:** Python 3.12+
* **Banco de Dados:** PostgreSQL (`psycopg2` com SQL nativo e `UPSERT`)
* **Orquestração & Mídias:** Docker, Docker Compose, n8n
* **APIs & Scraping:** YouTube Data API v3, Shopee GraphQL, BeautifulSoup4, Requests
* **Arquitetura:** Clean Architecture / Layered Architecture (Divisão estrita em Models, Services, Repositories, Providers e Pipelines).

---

## Arquitetura do Sistema

```text
[ Promobit / Shopee ] ──(Scraper)──► [ Product Pipeline ]
                                            │
                                            ├──► [ Postgres Database ] (UPSERT)
                                            │
                                     (Normalizador)
                                            │
                                            ▼
[ YouTube Data API ] ◄──(Scoring)─── [ Video Service ]
                                            │
                                            ▼
                                   [ Contexto Unificado ] ──► [ Workflows n8n ]


## Estrutura do Projeto
python/app/
├── core/         # Módulos base (DB connection, Logger, Migrations)
├── models/       # Entidades de Domínio (Product, Video, Publication)
├── scrapers/     # Módulos de extração web (Promobit, Shopee)
├── providers/    # Clientes de APIs externas (YouTube API, Shopee GraphQL)
├── repositories/ # Camada de acesso a dados (SQL Queries)
├── services/     # Regras de negócio (Scoring, Normalização, Categorização)
└── pipelines/    # Orquestração do fluxo ponta a ponta

## Como Executar o Projeto

Pré-requisitos
Docker e Docker Compose instalados.

Passos:

1- Clone o repositório:

Bash:
git clone [https://github.com/seu-usuario/ShopeeAffiliate.git](https://github.com/seu-usuario/ShopeeAffiliate.git)
cd ShopeeAffiliate

2- Configure as variáveis de ambiente:

Bash:
cp .env.example .env
# Adicione suas chaves do YouTube e Shopee no arquivo .env

3- Suba o ambiente com Docker:

Bash:
docker-compose up -d --build
4- Execute as migrações do banco de dados:

Bash:
docker exec -it shopee_python python -m app.commands.migrate

5- Rode o pipeline de teste completo:

Bash:
docker exec -it shopee_python python -m tests.test_scraper_completo


