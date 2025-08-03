
import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
''')
cursor.execute("INSERT INTO users (name, email, password) VALUES ('John Doe', 'john@example.com', 'password123')")
cursor.execute("INSERT INTO users (name, email, password) VALUES ('Jane Smith', 'jane@example.com', 'secret456')")
cursor.execute("INSERT INTO users (name, email, password) VALUES ('Bob Johnson', 'bob@example.com', 'qwerty789')")

users = [
    ("John Doe", "john@example.com", generate_password_hash("password123")),
    ("Jane Smith", "jane@example.com", generate_password_hash("secret456")),
    ("Bob Johnson", "bob@example.com", generate_password_hash("qwerty789")),
]

cursor.executemany("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", users)

conn.commit()
conn.close()

print("Database initialized with sample data")
print("Database initialized with sample data (hashed passwords)")