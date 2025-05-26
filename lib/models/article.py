from lib.db.connection import get_connection

class articles:
    def _init_(self, id, title, author_id, magazine_id)
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id
    
    def articles(self);
        conn= get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?""")
        return cursor.fetchall()