import psycopg

conn = psycopg.connect(
    "postgresql://postgres:postgres@localhost:5432/tasksdb"
)

cur = conn.cursor()

cur.execute(
    "INSERT INTO tasks (title, done) VALUES (%s, %s)",
    ("Docker test task", False)
)

conn.commit()

cur.execute("SELECT * FROM tasks")

for row in cur.fetchall():
    print(row)

cur.close()
conn.close()