class articles:
    def articles(self);
        conn= get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?""")
        return cursor.fetchall()