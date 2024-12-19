from __future__ import annotations

from typing import Optional

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


class SingletonMeta(type):
    _instance: Optional[Singleton] = None

    def __call__(self) -> Singleton:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Singleton(metaclass=SingletonMeta):
    def database_connection(self):
        db = SQLAlchemy()
        return db

    # https://flask-migrate.readthedocs.io/en/latest/
    def migration(self):
        migrate = Migrate()
        return migrate
