import pytest
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

def test_magazine_save_and_find_by_name():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM magazines")
    conn.commit()

    mag = Magazine(name="TechLife", category="Technology")
    mag.save()

    found = Magazine.find_by_name("TechLife")
    assert found.name == "TechLife"
    assert found.category == "Technology"
