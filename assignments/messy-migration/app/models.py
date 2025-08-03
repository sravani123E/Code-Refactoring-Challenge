import sqlite3
from app.db import get_cursor

# User model functions

def get_all_users():
    with get_cursor() as (cursor, _):
        cursor.execute("SELECT id, name, email FROM users")
        return cursor.fetchall()

def get_user_by_id(user_id):
    with get_cursor() as (cursor, _):
        cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()

def create_user(name, email, password_hash):
    with get_cursor() as (cursor, _):
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (name, email, password_hash)
        )
        return cursor.lastrowid

def update_user(user_id, name, email):
    with get_cursor() as (cursor, _):
        cursor.execute(
            "UPDATE users SET name = ?, email = ? WHERE id = ?",
            (name, email, user_id)
        )
        return cursor.rowcount

def delete_user(user_id):
    with get_cursor() as (cursor, _):
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        return cursor.rowcount

def search_users_by_name(name):
    with get_cursor() as (cursor, _):
        cursor.execute("SELECT id, name, email FROM users WHERE name LIKE ?", (f"%{name}%",))
        return cursor.fetchall()

def get_user_by_email(email):
    with get_cursor() as (cursor, _):
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        return cursor.fetchone()
