import psycopg

conn = psycopg.connect(
    "postgresql://postgres:postgres@localhost:5432/tasksdb"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL DEFAULT FALSE
);
""")

conn.commit()

cur.close()
conn.close()

print("Table created successfully!")