from lib.db.connection import get_connection  # Make sure this import matches your project structure

class author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def add_author_with_articles(author_name, articles_data):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO authors (name) VALUES (?)", (author_name,))
            author_id = cursor.fetchone()[0]
            for article in articles_data:
                cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", (article['title'], author_id, article['magazine-id']))
            conn.execute("COMMIT")
            return True
        except Exception as e:
            conn.execute("ROLLBACK")
            print(f"Transaction failed: {e}")