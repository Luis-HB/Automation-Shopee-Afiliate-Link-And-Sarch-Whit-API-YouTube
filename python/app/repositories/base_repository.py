from psycopg2 import sql

from core.database import get_connection


class Repository:

    def __init__(self, table, model):

        self.conn = get_connection()
        self.cursor = self.conn.cursor()

        self.table = table
        self.model = model

        self._where = []
        self._params = []

        self._order = ""
        self._limit = ""

    # --------------------------
    # Query Builder
    # --------------------------

    def where(self, column, value):

        self._where.append(f"{column}=%s")
        self._params.append(value)

        return self

    def order_by(self, column, direction="ASC"):

        self._order = f" ORDER BY {column} {direction}"

        return self

    def limit(self, value):

        self._limit = f" LIMIT {value}"

        return self

    # --------------------------
    # SELECT
    # --------------------------

    def get(self):

        query = f"SELECT * FROM {self.table}"

        if self._where:
            query += " WHERE " + " AND ".join(self._where)

        query += self._order
        query += self._limit

        self.cursor.execute(query, self._params)

        rows = self.cursor.fetchall()

        self._clear()

        return [self.model.from_dict(row) for row in rows]

    def first(self):

        self.limit(1)

        rows = self.get()

        if rows:
            return rows[0]

        return None

    # --------------------------
    # INSERT
    # --------------------------

    def save(self, obj):

        data = obj.__dict__.copy()

        data.pop("id", None)

        columns = list(data.keys())

        values = list(data.values())

        query = sql.SQL(
            """
            INSERT INTO {} ({})
            VALUES ({})
            RETURNING id
            """
        ).format(
            sql.Identifier(self.table),
            sql.SQL(",").join(map(sql.Identifier, columns)),
            sql.SQL(",").join(sql.Placeholder() * len(columns)),
        )

        self.cursor.execute(query, values)

        obj.id = self.cursor.fetchone()["id"]

        self.conn.commit()

        return obj

    # --------------------------
    # UPDATE
    # --------------------------

    def update(self, obj):

        data = obj.__dict__.copy()

        obj_id = data.pop("id", None)

        if obj_id is None:
            raise ValueError("Objeto sem ID.")

        columns = list(data.keys())

        values = list(data.values())

        query = sql.SQL(
            """
            UPDATE {}

            SET {}

            WHERE id=%s
            """
        ).format(
            sql.Identifier(self.table),
            sql.SQL(",").join(
                sql.SQL("{}=%s").format(sql.Identifier(col))
                for col in columns
            ),
        )

        values.append(obj_id)

        self.cursor.execute(query, values)

        self.conn.commit()

    # --------------------------

    def delete(self, id):

        self.cursor.execute(

            f"DELETE FROM {self.table} WHERE id=%s",

            (id,)

        )

        self.conn.commit()

    # --------------------------

    def find_by(self, column, value):

        return self.where(column, value).first()

    # --------------------------

    def all(self):

        return self.get()

    # --------------------------

    def close(self):

        self.cursor.close()
        self.conn.close()

    # --------------------------

    def _clear(self):

        self._where = []
        self._params = []
        self._order = ""
        self._limit = ""


    def upsert(self, obj, conflict_column="hash_produto"):

        data = obj.__dict__.copy()

        # remove campos automáticos
        data.pop("id", None)
        data.pop("created_at", None)
        data.pop("updated_at", None)

        columns = list(data.keys())
        values = list(data.values())

        updates = []

        for col in columns:

            if col != conflict_column:

                updates.append(

                    sql.SQL("{} = EXCLUDED.{}").format(

                        sql.Identifier(col),

                        sql.Identifier(col)

                    )

                )

        # atualiza automaticamente a data
        updates.append(

            sql.SQL("updated_at = NOW()")

        )

        query = sql.SQL("""
            INSERT INTO {table} ({columns})
            VALUES ({values})

            ON CONFLICT ({conflict})

            DO UPDATE SET

            {updates}

            RETURNING id
        """).format(

            table=sql.Identifier(self.table),

            columns=sql.SQL(",").join(
                map(sql.Identifier, columns)
            ),

            values=sql.SQL(",").join(
                sql.Placeholder() * len(columns)
            ),

            conflict=sql.Identifier(conflict_column),

            updates=sql.SQL(",").join(updates)

        )

        self.cursor.execute(query, values)

        row = self.cursor.fetchone()

        obj.id = row["id"]

        self.conn.commit()

        return obj