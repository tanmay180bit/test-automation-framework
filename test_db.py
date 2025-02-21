import pytest
import sqlite3

@pytest.fixture
def db_conn():
    """Fixture to provide a fresh database connection."""
    conn = sqlite3.connect(":memory:")  # Use in-memory DB for testing
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE)")
    
    yield conn  # Provide the connection to test functions
    
    conn.close()  # Cleanup after test


def test_database_connection(db_conn):
    """Test if the database connection is working."""
    assert db_conn is not None


def test_fetch_users(db_conn):
    """Test fetching users from the database."""
    cursor = db_conn.cursor()
    
    # Clear table before inserting test data
    cursor.execute("DELETE FROM users")
    
    # Insert test user
    cursor.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')")
    db_conn.commit()
    
    # Fetch users
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    assert len(users) > 0  # Ensure at least one user exists


def test_insert_user(db_conn):
    """Test inserting a new user into the database."""
    cursor = db_conn.cursor()

    # Clear table before inserting
    cursor.execute("DELETE FROM users")
    
    cursor.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')")
    db_conn.commit()

    # Verify the insertion
    cursor.execute("SELECT * FROM users WHERE email = 'alice@example.com'")
    user = cursor.fetchone()

    assert user is not None
    assert user[1] == "Alice"  # Use index instead of dict key


def test_delete_user(db_conn):
    """Test deleting a user from the database."""
    cursor = db_conn.cursor()
    
    # Clear table and insert user
    cursor.execute("DELETE FROM users")
    cursor.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')")
    db_conn.commit()

    # Delete user
    cursor.execute("DELETE FROM users WHERE email = 'alice@example.com'")
    db_conn.commit()

    # Verify deletion
    cursor.execute("SELECT * FROM users WHERE email = 'alice@example.com'")
    user = cursor.fetchone()

    assert user is None  # User should be deleted
