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

    "commercial_agent": os.getenv(

        "N8N_COMMERCIAL_AGENT",

        "http://n8n:5678/webhook/commercial-analysis"

    ),

    "caption_agent": os.getenv(

        "N8N_CAPTION_AGENT",

        "http://n8n:5678/webhook/generate-caption"

    ),

    "script_agent": os.getenv(

        "N8N_SCRIPT_AGENT",

        "http://n8n:5678/webhook/generate-script"

    ),

    "publication_agent": os.getenv(

        "N8N_PUBLICATION_AGENT",

        "http://n8n:5678/webhook/publication"

    ),

    "timeout": int(

        os.getenv(

            "N8N_TIMEOUT",

            "300"

        )

    ),

    "verify_ssl": os.getenv(

        "N8N_VERIFY_SSL",

        "false"

    ).lower() == "true"

}

# ======================================================
# Ambiente
# ======================================================

DEBUG = os.getenv(

    "DEBUG",

    "False"

).lower() == "true"