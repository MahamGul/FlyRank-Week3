import os
import time
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def get_connection():
    for attempt in range(10):
        try:
            return psycopg.connect(
                DATABASE_URL,
                row_factory=dict_row
            )
        except psycopg.OperationalError:
            if attempt == 9:
                raise
            time.sleep(2)


def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT FALSE
        )
    """)

    conn.commit()
    conn.close()


def seed_data():
    conn = get_connection()

    count = conn.execute(
        "SELECT COUNT(*) AS count FROM tasks"
    ).fetchone()["count"]

    if count == 0:
        with conn.cursor() as cur:
            cur.executemany(
                "INSERT INTO tasks (title, done) VALUES (%s, %s)",
                [
                    ("Learn FastAPI", False),
                    ("Build CRUD API", True),
                    ("Connect PostgreSQL", False),
                ]
            )

        conn.commit()

    conn.close()