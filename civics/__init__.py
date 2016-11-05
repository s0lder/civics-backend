from flask import Flask
from peewee import SqliteDatabase

from .db import Database


def create_app(name):
    app = Flask(name)
    app.config.from_object('civics.config.DevConfig')
    return app


app = create_app(__name__)
database = Database(app, SqliteDatabase(app.config['DATABASE_FILENAME']))

import civics.views
