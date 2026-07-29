from database import get_connection
from repositories.task_repository import TaskRepository


class PostgresTaskRepository(TaskRepository):

    def get_all_tasks(self):
        conn = get_connection()

        rows = conn.execute(
            "SELECT * FROM tasks ORDER BY id"
        ).fetchall()

        conn.close()

        return rows

    def get_task_by_id(self, task_id):
        conn = get_connection()

        row = conn.execute(
            "SELECT * FROM tasks WHERE id = %s",
            (task_id,)
        ).fetchone()

        conn.close()

        return row

    def create_task(self, title):
        conn = get_connection()

        row = conn.execute(
            """
            INSERT INTO tasks (title, done)
            VALUES (%s, %s)
            RETURNING *
            """,
            (title, False)
        ).fetchone()

        conn.commit()
        conn.close()

        return row

    def update_task(self, task_id, title=None, done=None):
        conn = get_connection()

        row = conn.execute(
            "SELECT * FROM tasks WHERE id = %s",
            (task_id,)
        ).fetchone()

        if not row:
            conn.close()
            return None

        current_title = row["title"]
        current_done = row["done"]

        if title is not None:
            current_title = title

        if done is not None:
            current_done = done

        updated_row = conn.execute(
            """
            UPDATE tasks
            SET title = %s, done = %s
            WHERE id = %s
            RETURNING *
            """,
            (current_title, current_done, task_id)
        ).fetchone()

        conn.commit()
        conn.close()

        return updated_row

    def delete_task(self, task_id):
        conn = get_connection()

        row = conn.execute(
            "SELECT * FROM tasks WHERE id = %s",
            (task_id,)
        ).fetchone()

        if not row:
            conn.close()
            return False

        conn.execute(
            "DELETE FROM tasks WHERE id = %s",
            (task_id,)
        )

        conn.commit()
        conn.close()

        return True