import sqlite3

# Connect to your database
conn = sqlite3.connect("database.db")  # Ensure this is the correct database file
cursor = conn.cursor()

# Check if the 'users' table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
table_exists = cursor.fetchone()

if table_exists:
    print("✅ The 'users' table exists!")
else:
    print("❌ The 'users' table does NOT exist. Please create it.")

conn.close()
