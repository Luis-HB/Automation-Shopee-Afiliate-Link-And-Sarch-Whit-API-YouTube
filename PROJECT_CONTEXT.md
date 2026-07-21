# 📄 Contexto do Projeto: ShopeeAffiliate

## 1. Visão Geral
O **ShopeeAffiliate** é uma aplicação de automação para marketing de afiliados (focado em Shopee/Promobit). O sistema faz a raspagem (scraping) de ofertas, extrai metadados do produto, resolve links de afiliados, busca vídeos relevantes de review/unboxing no YouTube, ranqueia esses vídeos por relevância via score e persiste o contexto completo no banco de dados para consumo por fluxos de automação (ex: n8n).

---

## 2. Tech Stack & Infraestrutura

* **Linguagem Principal:** Python 3.12+
* **Banco de Dados:** PostgreSQL (com suporte a conexões nativas via `psycopg2`)
* **Orquestração:** Docker & Docker Compose
* **Integrações Externa:**
  * **Shopee:** API GraphQL (Short Links e Conversões de Afiliados)
  * **YouTube:** Data API v3 (Busca, Scoring e Métricas de Vídeos)
  * **Promobit:** Scraping de Ofertas Promocionais
* **Automação de Workflows:** n8n e pgAdmin incorporados via containers

---

## 3. Arquitetura de Pastas (`python/app/`)

O projeto adota os princípios de **Clean Architecture / Layered Architecture**:

```text
python/app/
├── commands/       # Scripts CLI para banco (migrate.py, seed.py, reset.py, status.py)
├── core/           # Módulos base (database.py, logger.py, exceptions.py, migration.py)
├── factories/      # Fabrica objetos a partir de dicionários/JSONs (ProductFactory, VideoFactory)
├── graphql/        # Queries e Mutations em arquivos .graphql nativos
├── models/         # Entidades do sistema (Product, Video, Publication, ProductContext)
├── pipelines/      # Orquestradores de ponta a ponta (AffiliatePipeline, ProductPipeline)
├── providers/      # Integrações com plataformas externas de vídeo (YouTubeProvider, ShopeeVideoProvider)
├── repositories/   # Camada de dados/SQL (ProductRepository, VideoRepository, PublicationRepository)
├── scrapers/       # Crawlers/Parsers (PromobitScraper, ShopeeScraper, RedirectParser)
├── services/       # Regras de Negócio organizadas por domínio:
│   ├── affiliate/   # Geração e resolução de links de afiliados
│   ├── context/     # Construção, enriquecimento e serialização do ProductContext
│   ├── product/     # Análise de produto, categorias e normalização
│   ├── publication/ # Geração de legendas e metadados para postagem
│   ├── ranking/     # Regras de pontuação e seleção dos melhores vídeos
│   ├── search/      # Construção de queries otimizadas de busca
│   └── video/       # Descoberta e consumo de serviços de vídeo
└── tests/          # Suíte de testes unitários e de integração end-to-end