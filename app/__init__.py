import os

from flask import Flask

from app.config import get_config
from app.extensions.db import db
from app.extensions.login_manager import login_manager
from app.routes.auth.routes import auth_bp
from app.routes.todo.routes import todo_bp
from app.schemas.user import User


def create_app():
    # Resolve project root explicitly
    # BASE_DIR = Path(__file__).resolve().parent.parent
    # env_path = BASE_DIR / ".env"
    #
    # load_dotenv(dotenv_path=env_path, override=True)

    app = Flask(__name__)

    # Load config based on FLASK_ENV
    config_class = get_config(os.getenv("FLASK_ENV", "development"))
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(todo_bp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
