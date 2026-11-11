import os
import sqlite3

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    current_app,
    jsonify
)

main = Blueprint("main", __name__)

PRIORITIES = ("High", "Medium", "Low")


# Connect to the SQLite database
def get_db():
    default_path = os.path.join(
        current_app.instance_path, "tasks.db"
    )

    db_path = current_app.config.get("DATABASE", default_path)

    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row

    return connection


# Create and update the database table
@main.before_app_request
def create_database():
    connection = get_db()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'Pending'
        )
    """)

    columns = [
        row["name"]
        for row in connection.execute(
            "PRAGMA table_info(tasks)"
        ).fetchall()
    ]

    if "priority" not in columns:
        connection.execute("""
            ALTER TABLE tasks
            ADD COLUMN priority TEXT NOT NULL DEFAULT 'Medium'
        """)

    if "start_date" not in columns:
        connection.execute("""
            ALTER TABLE tasks
            ADD COLUMN start_date TEXT
        """)

    if "end_date" not in columns:
        connection.execute("""
            ALTER TABLE tasks
            ADD COLUMN end_date TEXT
        """)

    connection.commit()
    connection.close()


# Display all tasks
@main.route("/")
def index():
    connection = get_db()

    tasks = connection.execute(
        "SELECT * FROM tasks ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return render_template("index.html", tasks=tasks)


# Add a new task
@main.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    priority = request.form.get("priority", "Medium")
    start_date = request.form.get("start_date", "")
    end_date = request.form.get("end_date", "")

    if priority not in PRIORITIES:
        priority = "Medium"

    if start_date and end_date and end_date < start_date:
        return "End date cannot be before start date.", 400

    if title:
        connection = get_db()

        connection.execute(
            """INSERT INTO tasks
            (title, description, priority, start_date, end_date)
            VALUES (?, ?, ?, ?, ?)""",
            (title, description, priority, start_date, end_date)
        )

        connection.commit()
        connection.close()

    return redirect(url_for("main.index"))


# Edit an existing task
@main.route("/edit/<int:task_id>", methods=["POST"])
def edit_task(task_id):
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    priority = request.form.get("priority", "Medium")
    start_date = request.form.get("start_date", "")
    end_date = request.form.get("end_date", "")

    if priority not in PRIORITIES:
        priority = "Medium"

    if start_date and end_date and end_date < start_date:
        return "End date cannot be before start date.", 400

    if title:
        connection = get_db()

        connection.execute(
            """UPDATE tasks
            SET title=?, description=?, priority=?,
                start_date=?, end_date=?
            WHERE id=?""",
            (title, description, priority, start_date, end_date, task_id)
        )

        connection.commit()
        connection.close()

    return redirect(url_for("main.index"))


# Mark a task as completed or pending
@main.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    connection = get_db()

    connection.execute(
        """UPDATE tasks SET status =
        CASE WHEN status = 'Pending'
        THEN 'Completed' ELSE 'Pending' END
        WHERE id = ?""",
        (task_id,)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("main.index"))


# Delete a task
@main.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    connection = get_db()

    connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("main.index"))


# Application health check
@main.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200
