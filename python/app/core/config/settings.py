import os

# ======================================================
# Banco
# ======================================================

DB_CONFIG = {

    "host": os.getenv("DB_HOST", "postgres"),

    "port": os.getenv("DB_PORT", "5432"),

    "database": os.getenv("DB_NAME", "shopee_affiliate"),

    "user": os.getenv("DB_USER", "admin"),

    "password": os.getenv("DB_PASSWORD", "123456"),

}

# ======================================================
# Shopee
# ======================================================

SHOPEE_CONFIG = {

    "endpoint": os.getenv("SHOPEE_GRAPHQL_ENDPOINT"),

    "app_id": os.getenv("SHOPEE_APP_ID"),

    "secret": os.getenv("SHOPEE_SECRET"),

}

# ======================================================
# YouTube
# ======================================================

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# ======================================================
# n8n
# ======================================================

N8N_CONFIG = {

    "publication_webhook": os.getenv(
        "N8N_PUBLICATION_WEBHOOK",
        "http://n8n:5678/webhook/publication"
    ),

}

# ======================================================
# Ambiente
# ======================================================

DEBUG = os.getenv("DEBUG", "False").lower() == "true"