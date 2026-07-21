from core.database import get_connection
from models.video import Video


class VideoRepository:

    def __init__(self):
        self.conn = get_connection()
        self.cur = self.conn.cursor()

    def upsert(self, video):

        try:
            self.cur.execute(
                """
                INSERT INTO videos_produto
                (
                    produto_id,
                    youtube_id,
                    titulo,
                    canal,
                    thumbnail,
                    url,
                    views,
                    likes,
                    duracao,
                    score
                )
                VALUES
                (
                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s
                )

                ON CONFLICT (youtube_id)

                DO UPDATE SET
                    produto_id = EXCLUDED.produto_id,
                    titulo = EXCLUDED.titulo,
                    canal = EXCLUDED.canal,
                    thumbnail = EXCLUDED.thumbnail,
                    url = EXCLUDED.url,
                    views = EXCLUDED.views,
                    likes = EXCLUDED.likes,
                    duracao = EXCLUDED.duracao,
                    score = EXCLUDED.score;
                """,
                (
                    video.produto_id,
                    video.youtube_id,
                    video.titulo,
                    video.canal,
                    video.thumbnail,
                    video.url,
                    video.views,
                    video.likes,
                    video.duracao,
                    video.score,
                ),
            )

            self.conn.commit()

        except Exception:
            self.conn.rollback()
            raise

    def close(self):
        self.cur.close()
        self.conn.close()

    def find_by_produto(self, produto_id):

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT *
            FROM videos_produto
            WHERE produto_id=%s
            ORDER BY score DESC
        """, (produto_id,))

        rows = cur.fetchall()

        cur.close()
        conn.close()

        return [Video.from_dict(row) for row in rows]