from psycopg2.errors import UndefinedTable
from core.database import get_connection


def run():

    conn = get_connection()
    cur = conn.cursor()

    try:

        cur.execute("""
            SELECT migration,
                   executed_at
            FROM schema_migrations
            ORDER BY id;
        """)

        rows = cur.fetchall()

    except UndefinedTable:

        print("\nNenhuma migration executada.\n")
        return

    print("\n===== MIGRATIONS =====")

    if not rows:
        print("Nenhuma migration executada.")

    for row in rows:
        print(f"{row['migration']} -> {row['executed_at']}")

    print()

    cur.close()
    conn.close()