import sqlite3
from contextlib import contextmanager

@contextmanager
def connect(db_path):
    """Context manager that yields a SQLite connection."""
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()

def get_first_table_name(conn):
    """Return the name of the first table in the SQLite database."""
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    row = cur.fetchone()
    return row[0] if row else None
