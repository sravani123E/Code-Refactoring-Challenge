import sqlite3
from contextlib import contextmanager

DB_PATH = 'users.db'

def get_connection():
    return sqlite3.connect(DB_PATH)

@contextmanager
def get_cursor():
    conn = get_connection()
    try:
        yield conn.cursor(), conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
