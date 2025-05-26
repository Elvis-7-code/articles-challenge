from lib.db.connection import get_connection

def setup_database():
    with open("lib/db/schema.sql") as f:
        schema = f.read()
    conn = get_connection()
    conn.excecutescript(schema)
    conn.commit()
    conn.close()

if _name_ == "_main_":
    setup_database        