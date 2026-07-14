from core.database import get_connection


def run():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""
        SELECT migration,
               executed_at
        FROM schema_migrations
        ORDER BY id;
    """)

    rows = cur.fetchall()

    print()

    print("===== MIGRATIONS =====")

    if not rows:
        print("Nenhuma migration executada.")

    for row in rows:
        print(f"{row[0]}  -> {row[1]}")

    print()

    cur.close()

    conn.close()