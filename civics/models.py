from peewee import create_model_tables

from . import database


def create_tables(fail_silently=False):
    models = database.Model.__subclasses__()
    create_model_tables(models, fail_silently=fail_silently)
