class magazines:
    def magazines(self):
        conn = get_connection()
        cursor = get_cursor()
        cursor.excecute("""SELECT DISTINCT m.* FROM magazines m JOIN articles a ON m.id = a.magazine_id WHERE a.author_id = ?""", (self.id,))
        return cursor.fetchall()