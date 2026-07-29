from core.database import get_connection
from models.video import Video


class VideoRepository:

    def __init__(self):

        self.conn = get_connection()
        self.cur = self.conn.cursor()

    # =====================================================
    # Persistência
    # =====================================================

    def upsert(self, video: Video):

        youtube_id = getattr(video, "youtube_id", None)

        if youtube_id is None:
            youtube_id = getattr(video, "video_id", None)

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
                    score = EXCLUDED.score

                RETURNING id;
                """,
                (
                    video.produto_id,
                    youtube_id,
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

            row = self.cur.fetchone()

            if row:
                video.id = row["id"]

            self.conn.commit()

            return video

        except Exception:

            self.conn.rollback()

            raise

    # =====================================================
    # Consultas
    # =====================================================

    def find_by_produto(self, produto_id):

        self.cur.execute(
            """
            SELECT *
            FROM videos_produto
            WHERE produto_id=%s
            ORDER BY score DESC
            """,
            (produto_id,),
        )

        rows = self.cur.fetchall()

        return [
            Video.from_dict(row)
            for row in rows
        ]

    # -----------------------------------------------------
    # Alias da arquitetura nova
    # -----------------------------------------------------

    def find_by_product(self, product_id):

        return self.find_by_produto(product_id)

    # =====================================================
    # Remoção
    # =====================================================

    def delete(self, video_id):

        self.cur.execute(
            """
            DELETE
            FROM videos_produto
            WHERE id=%s
            """,
            (video_id,),
        )

        self.conn.commit()

    # =====================================================

    def close(self):

        self.cur.close()

        self.conn.close()