from pathlib import Path

from core.database import get_connection
from core.logger import Logger

MIGRATIONS_PATH = Path("/database/migrations")


def create_schema_table(cursor):

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS schema_migrations (

            id SERIAL PRIMARY KEY,

            migration VARCHAR(255) UNIQUE,

            executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        );

    """)


def already(cursor, migration):

    cursor.execute(

        "SELECT 1 FROM schema_migrations WHERE migration=%s",

        (migration,)

    )

    return cursor.fetchone() is not None


def register(cursor, migration):

    cursor.execute(

        "INSERT INTO schema_migrations (migration) VALUES (%s)",

        (migration,)

    )


def execute_migrations():

    conn = get_connection()

    cur = conn.cursor()

    create_schema_table(cur)

    conn.commit()

    files = sorted(MIGRATIONS_PATH.glob("*.sql"))

    Logger.info(f"{len(files)} migrations encontradas")

    for file in files:

        if already(cur, file.name):

            Logger.warning(f"{file.name} já executada")

            continue

        try:

            Logger.info(f"Executando {file.name}")

            sql = file.read_text(encoding="utf8")

            cur.execute(sql)

            register(cur, file.name)

            conn.commit()

            Logger.success(file.name)

        except Exception as e:

            conn.rollback()

            Logger.error(e)

            raise

    cur.close()

    conn.close()