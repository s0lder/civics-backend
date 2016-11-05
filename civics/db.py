from peewee import Model


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
            class Meta:
                database = self.database
        return FlaskModel
