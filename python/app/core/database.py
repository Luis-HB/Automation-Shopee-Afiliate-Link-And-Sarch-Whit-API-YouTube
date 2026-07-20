import psycopg2

from psycopg2.extras import RealDictCursor

from python.app.core.config.settings import DB_CONFIG


def get_connection():

    return psycopg2.connect(

        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],

        cursor_factory=RealDictCursor

    )