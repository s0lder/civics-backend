class DevConfig:
    DEBUG = True
    DATABASE_FILENAME = 'civics.db'
    SECRET_KEY = 'secret'
    STATIC_DIR = 'static/'


class Config(DevConfig):
    pass
