import sqlite3
from .databaseConnection import get_connection


def create_task(task):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO task (title, description, due_date)
            VALUES (?, ?, ?)
            """,
            (task.title, task.description, task.due_date)
        )

        conn.commit()
        task_id = cursor.lastrowid

        return {
            "id": task_id,
            "title": task.title,
            "description": task.description,
            "due_date": task.due_date,
            "status": "pending"
        }

    except sqlite3.Error as e:
        raise RuntimeError("Failed to create task") from e
    finally:
        if conn:
            conn.close()


def get_tasks():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        rows = cursor.execute("SELECT * FROM task").fetchall()
        return [dict(row) for row in rows]

    except sqlite3.Error as e:
        raise RuntimeError("Failed to fetch tasks") from e
    finally:
        if conn:
            conn.close()


def get_task_by_id(task_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        row = cursor.execute(
            "SELECT * FROM task WHERE id = ?",
            (task_id,)
        ).fetchone()
        return dict(row) if row else None

    except sqlite3.Error as e:
        raise RuntimeError("Failed to fetch task") from e
    finally:
        if conn:
            conn.close()


def update_task(task_id: int, task):
    try:
        data = task.model_dump(exclude_unset=True)
        if not data:
            return None  # Edge case: empty update payload

        conn = get_connection()
        cursor = conn.cursor()

        fields = ", ".join([f"{k} = ?" for k in data.keys()])
        values = list(data.values()) + [task_id]

        cursor.execute(
            f"UPDATE task SET {fields} WHERE id = ?",
            values
        )

        if cursor.rowcount == 0:
            return None

        conn.commit()
        return get_task_by_id(task_id)

    except sqlite3.Error as e:
        raise RuntimeError("Failed to update task") from e
    finally:
        if conn:
            conn.close()


def delete_task(task_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM task WHERE id = ?", (task_id,))
        conn.commit()
        return cursor.rowcount

    except sqlite3.Error as e:
        raise RuntimeError("Failed to delete task") from e
    finally:
        if conn:
            conn.close()
