from core.database import get_connection


class CategoryRepository:

    def __init__(self):
        self.conn = get_connection()
        self.cur = self.conn.cursor()

    def get_all(self):
        """Retorna todas as categorias ativas."""
        self.cur.execute(
            "SELECT id, nome, slug FROM categorias WHERE ativa = TRUE ORDER BY prioridade ASC"
        )
        rows = self.cur.fetchall()
        
        # Mapeia os resultados para dicionários
        return [{"id": row[0], "nome": row[1], "slug": row[2]} for row in rows]

    def close(self):
        self.cur.close()
        self.conn.close()