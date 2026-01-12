from flask import Blueprint, render_template
todo_bp = Blueprint('todo', __name__, url_prefix='/todos')


@todo_bp.get('/')
def get_todos():
    todos = [
        {
            "id": 1,
            "title": "Finish Flask MVC structure",
            "description": "Clean separation of routes, services, models",
            "priority": 1,
            "due_date": "2026-01-15",
            "is_completed": False,
        },
        {
            "id": 2,
            "title": "Build dashboard UI",
            "description": "Bootstrap 5 cards and modals",
            "priority": 3,
            "due_date": None,
            "is_completed": False,
        },
        {
            "id": 3,
            "title": "JWT authentication",
            "description": "Login, register, protect APIs",
            "priority": 2,
            "due_date": "2026-01-20",
            "is_completed": True,
        },
        {
            "id": 4,
            "title": "Write automated tests",
            "description": "Pytest unit and integration tests",
            "priority": 5,
            "due_date": None,
            "is_completed": False,
        },
        {
            "id": 5,
            "title": "Deployment prep",
            "description": "Gunicorn, config hardening",
            "priority": 4,
            "due_date": "2026-01-25",
            "is_completed": False,
        },
    ]
    return render_template('todo/index.html', todos=todos)

@todo_bp.post('/')
def create_todo():
    # Update logic here
    return "Todo Created!"

@todo_bp.patch('/')
def update_todo():
    # Update logic here
    return "Todo Updated!"

@todo_bp.delete('/')
def delete_todo():
    # Update logic here
    return "Todo Deleted!"