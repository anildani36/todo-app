from flask import Blueprint, flash, redirect, request, url_for
from flask_login import login_required, current_user
from flask_pydantic import validate

from app.models.todo_models import TodoItem
from app.services.todo_service import TodoService

todo_bp = Blueprint('todo', __name__, url_prefix='/todos')


@todo_bp.get('/')
@login_required
def get_todos():
    user_id: int = current_user.get_id()
    return TodoService().fetch_todos(user_id=user_id)


@todo_bp.post('/')
@login_required
@validate()
def create_todo(form: TodoItem):
    user_id: int = current_user.get_id()
    return TodoService().create_todo(todo_item= form, user_id=user_id)


@todo_bp.post('/update/<int:todo_id>')
@login_required
@validate()
def update_todo(todo_id: int, form: TodoItem):
    user_id: int = current_user.get_id()
    return TodoService().update_todo(todo_id=todo_id, user_id=user_id, todo_item=form)


@todo_bp.post('/delete/<int:todo_id>')
@login_required
def delete_todo(todo_id: int):
    # Check for DELETE method override from HTML form
    if request.form.get('_method') != 'DELETE':
        flash("Invalid request method", "danger")
        return redirect(url_for('todo.get_todos'))

    user_id: int = current_user.get_id()
    return TodoService().delete_todo(todo_id=todo_id, user_id=user_id)
