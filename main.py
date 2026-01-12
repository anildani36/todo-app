from flask import Flask, render_template

from routes.auth.routes import auth_bp
from routes.todo.routes import todo_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(todo_bp)

@app.route('/todos', methods=['GET', 'POST'])
def todo():
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

@app.route('/password_reset')
def password_reset():
    return "<h1>Password reset</h1>"

if __name__ == "__main__":
    app.run(debug=True)
