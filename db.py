import sqlite3

def get_db_connection(testing=False):
    """Create a connection to the SQLite database"""
    if testing:
        conn = sqlite3.connect(":memory:")  # Use an in-memory DB for tests
    else:
        conn = sqlite3.connect("database.db")

    conn.row_factory = sqlite3.Row  # Allows dictionary-like row access
    return conn

def create_table(conn):
    """Create a users table if it doesn't exist"""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
