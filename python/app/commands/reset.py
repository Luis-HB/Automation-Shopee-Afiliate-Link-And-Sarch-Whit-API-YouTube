from core.database import get_connection


def run():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

    DROP SCHEMA public CASCADE;

    CREATE SCHEMA public;

    """)

    conn.commit()

    print("Banco resetado.")

    cur.close()

    conn.close()