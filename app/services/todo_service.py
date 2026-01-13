import logging
from flask import flash, render_template, redirect, url_for
from app import db
from app.schemas.todo import Todo
from app.models.todo_models import TodoItem

logger = logging.getLogger(__name__)
class TodoService:
    @staticmethod
    def fetch_todos(user_id: int):
        try:
            logger.info(f"Fetching todos for user {user_id}")
            todos = Todo.query.filter_by(user_id=user_id).order_by(Todo.created_at.desc()).all()
            logger.info(f"Found {len(todos)} todos for user {user_id}")
            return render_template("todo/todos.html", todos=todos)
        except Exception as e:
            logging.error(f"Error fetching todos for user {user_id}: {e}")
            flash("Could not load your todos.", "danger")
            return render_template("todo/todos.html", todos=[])

    @staticmethod
    def create_todo(todo_item: TodoItem, user_id: int):
        try:
            logger.info(f"Creating new todo for user {user_id}: {todo_item.title}")
            db.session.add(Todo(
                title=todo_item.title,
                description=todo_item.description,
                priority=todo_item.priority,
                due_date=todo_item.due_date,
                user_id=user_id
            ))
            db.session.commit()
            logger.info(f"Todo for user {user_id} created successfully: {todo_item.title}")
            flash("Task created successfully!", "success")
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error creating todo for user {user_id} with title {todo_item.title}: {e}")
            flash("Error saving task.", "danger")
        return redirect(url_for('todo.get_todos'))

    @staticmethod
    def update_todo(todo_id: int, user_id: int, todo_item: TodoItem):
        try:
            logger.info(f"Updating todo for user {user_id} with id {todo_id}: {todo_item.title}")
            todo = Todo.query.filter_by(id=todo_id, user_id=user_id).first()
            if not todo:
                logger.warning(f"Task not found or access denied while updating todo for user {user_id} with id {todo_id}: {todo_item.title}.")
                flash("Task not found or access denied.", "danger")
                return redirect(url_for('todo.get_todos'))

            todo.title = todo_item.title
            todo.description = todo_item.description
            todo.priority = todo_item.priority
            todo.due_date = todo_item.due_date

            db.session.commit()
            logger.info(f"Todo for user {user_id} with id {todo_id} updated successfully: {todo_item.title}")
            flash("Task updated!", "success")
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error updating todo for user {user_id} with id {todo_id}: {e}")
            flash("Error updating task.", "danger")
        return redirect(url_for('todo.get_todos'))

    @staticmethod
    def delete_todo(todo_id: int, user_id: int):
        try:
            logger.info(f"Deleting todo for user {user_id} with id {todo_id}")
            todo = Todo.query.filter_by(id=todo_id, user_id=user_id).first()
            if not todo:
                logger.warning(f"Access denied while deleting todo for user {user_id} with id {todo_id}")
                flash("Access denied.", "danger")
                return redirect(url_for('todo.get_todos'))

            db.session.delete(todo)
            db.session.commit()
            logger.info(f"Deleted todo for user {user_id} with id {todo_id} successfully!")
            flash("Task deleted.", "info")
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error deleting todo {todo_id} for user {user_id}: {e}")
            flash("Error deleting task.", "danger")
        return redirect(url_for('todo.get_todos'))
