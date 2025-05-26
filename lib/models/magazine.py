from lib.db.connection import get_connection, get_cursor
class magazines:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category


    def magazines(self):
        conn = get_connection()
        cursor = get_cursor()
        cursor.excecute("""SELECT DISTINCT m.* FROM magazines m JOIN articles a ON m.id = a.magazine_id WHERE a.author_id = ?""", (self.id,))
        return cursor.fetchall()