from app.config.development import DevelopmentConfig
from app.config.testing import TestingConfig
from app.config.base import BaseConfig


def get_config(env: str):
    configs = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": BaseConfig,
    }
    return configs.get(env, DevelopmentConfig)
