import logging

from flask import flash, redirect, url_for
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions.db import db
from app.models.auth_models import LoginRequest, RegisterRequest
from app.schemas.user import User

logger = logging.getLogger(__name__)


class AuthService:

    def __init__(self):
        pass

    @staticmethod
    def authenticate_user(credentials: LoginRequest):
        logger.info(f"Authenticating user {credentials.username}")
        try:
            user = User.query.filter_by(email=credentials.email).first()

            if user and check_password_hash(user.password, credentials.password):
                logger.info(f"Authenticated user {credentials.username} successfully!")
                login_user(user)
                flash("Login successful!", "success")
                return redirect(url_for("todo.get_todos"))

            flash("Invalid username or password", "danger")
            logger.warning(f"Invalid username or password")
            return redirect(url_for("auth.show_login"))

        except Exception as e:
            logging.error(f"An error occurred during user login for {credentials.email}: {e}")
            flash("An error occurred. Please try again.", "danger")
            return redirect(url_for("auth.show_login"))

    @staticmethod
    def register_user(credentials: RegisterRequest):
        try:
            # Check if user already exists
            logger.info(f"Registering user {credentials.username}")
            existing_user = User.query.filter_by(email=credentials.email).first()
            if existing_user:
                flash("Email already registered. Please login.", "warning")
                logger.warning(f"Email {credentials.email} already registered. Please login.")
                return redirect(url_for("auth.register"))

            hashed_password = generate_password_hash(credentials.password)
            new_user = User(email=credentials.email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            flash("User registration successful!", "success")
            logger.info(f"User registration successful for user {credentials.email}")
            return redirect(url_for("auth.login"))

        except Exception as e:
            # Rollback the session
            db.session.rollback()
            logging.error(f"An error occurred during user registration for {credentials.email}: {e}")
            flash("An error occurred. Please try again.", "danger")
            return redirect(url_for("auth.register"))
