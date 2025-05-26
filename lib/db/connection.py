import sqlite3
CONN = sqlite3.connect('db/articles.db')
CURSOR = CONN.cursor()
def get_connection():
    conn = sqlite3.connect('articles.db')
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    return CONN
def get_cursor():
    return CURSOR