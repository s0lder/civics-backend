from peewee import Model
from playhouse.shortcuts import model_to_dict


class Database:
    def __init__(self, app, database):
        self.app = app
        self.database = database

        self.create_handlers()
        self.Model = self.get_model()

    def connect(self):
        self.database.connect()

    def close(self, exc):
        self.database.close()

    def create_handlers(self):
        self.app.before_request(self.connect)
        self.app.teardown_request(self.close)

    def get_model(self):
        class FlaskModel(Model):
            def json(self):
                return model_to_dict(self)

            class Meta:
                database = self.database
        return FlaskModel
