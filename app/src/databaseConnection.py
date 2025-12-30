import sqlite3
import os

DB_NAME = os.getenv("DB_NAME", "todo.db")

def get_connection():
    try:
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        # DB connection errors should bubble up
        raise RuntimeError("Database connection failed") from e


def init_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS task (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                due_date TEXT,
                status TEXT DEFAULT 'pending'
            )
            """
        )

        conn.commit()
    except sqlite3.Error as e:
        raise RuntimeError("Database initialization failed") from e
    finally:
        if conn:
            conn.close()
