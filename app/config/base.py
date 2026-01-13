import os


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///todo.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
