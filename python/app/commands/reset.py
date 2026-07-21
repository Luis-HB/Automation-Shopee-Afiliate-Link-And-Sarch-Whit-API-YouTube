from core.database import get_connection


def run():

    conn = get_connection()
    cur = conn.cursor()

    try:

        cur.execute("""
            DROP SCHEMA public CASCADE;
            CREATE SCHEMA public;
        """)

        conn.commit()

        print("Banco resetado.")

    except Exception:

        conn.rollback()
        raise

    finally:

        cur.close()
        conn.close()