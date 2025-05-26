import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection

def test_article_creation():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    cursor.execute("DELETE FROM articles")
    conn.commit()

    author = Author(name="Elvis")
    author.save()

    mag = Magazine(name="DevWorld", category="Coding")
    mag.save()

    article = Article(title="Debugging Tips", author_id=author.id, magazine_id=mag.id)
    article.save()

    articles = Article.find_by_author_id(author.id)
    assert any(a.title == "Debugging Tips" for a in articles)
