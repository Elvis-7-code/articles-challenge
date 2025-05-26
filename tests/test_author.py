import pytest
from lib.models.author import Author
from lib.db.connection import get_connection

def test_author_save_and_find_by_name():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM authors")  # Clean up
    conn.commit()

    author = Author(name="Elvis")
    author.save()

    found = Author.find_by_name("Elvis")
    assert found is not None
    assert found.name == "Elvis"
