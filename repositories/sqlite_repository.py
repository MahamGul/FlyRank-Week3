from database import get_connection
from repositories.task_repository import TaskRepository


class SQLiteTaskRepository(TaskRepository):

    def get_all_tasks(self):
        conn = get_connection()

        rows = conn.execute(
            "SELECT * FROM tasks"
        ).fetchall()

        conn.close()

        return [dict(row) for row in rows]

    def get_task_by_id(self, task_id):
        conn = get_connection()

        row = conn.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (task_id,)
        ).fetchone()

        conn.close()

        if row:
            return dict(row)

        return None

    def create_task(self, title):
        conn = get_connection()

        cursor = conn.execute(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            (title, False)
        )

        conn.commit()

        task_id = cursor.lastrowid

        row = conn.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (task_id,)
        ).fetchone()

        conn.close()

        return dict(row)

    def update_task(self, task_id, title=None, done=None):
        conn = get_connection()

        row = conn.execute(
            "SELECT * FROM tasks WHERE id = ?",
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

        conn.execute(
            """
            UPDATE tasks
            SET title = ?, done = ?
            WHERE id = ?
            """,
            (current_title, current_done, task_id)
        )

        conn.commit()

        updated_row = conn.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (task_id,)
        ).fetchone()

        conn.close()

        return dict(updated_row)

    def delete_task(self, task_id):
        conn = get_connection()

        row = conn.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (task_id,)
        ).fetchone()

        if not row:
            conn.close()
            return False

        conn.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

        conn.commit()
        conn.close()

        return True