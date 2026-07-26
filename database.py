import sqlite3
import os
DB_NAME = "tasks.db"
print("DATABASE PATH:", os.path.abspath(DB_NAME))

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL
        )
    """)

    conn.commit()

def seed_data():
    conn = get_connection()

    count = conn.execute(
        "SELECT COUNT(*) FROM tasks"
    ).fetchone()[0]

    if count == 0:
        example_tasks = [
            ("Learn FastAPI", False),
            ("Build CRUD API", True),
            ("Connect SQLite", False)
        ]

        conn.executemany(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            example_tasks
        )

        conn.commit()

    conn.close()

