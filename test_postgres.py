import psycopg

conn = psycopg.connect(
    "postgresql://postgres:postgres@localhost:5432/tasksdb"
)

cur = conn.cursor()
cur.execute("SELECT version();")

print(cur.fetchone())

cur.close()
conn.close()