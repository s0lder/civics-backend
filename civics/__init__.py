from flask import Flask
from peewee import SqliteDatabase

from .config.config import Config
from .db import Database


def create_app(name):
    app = Flask(name, static_folder=Config.STATIC_DIR)
    app.config.from_object('civics.config.config.Config')
    app.config.from_object('civics.config.apikeys')
    return app


app = create_app(__name__)
database = Database(app, SqliteDatabase(app.config['DATABASE_FILENAME']))

import civics.views
