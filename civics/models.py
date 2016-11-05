from peewee import *
from peewee import create_model_tables

from . import database


class Representative(database.Model):
    name = CharField()
    email = CharField()


class District(database.Model):
    number = IntegerField()
    representative = ForeignKeyField(Representative, related_name='district', unique=True)


class Story(database.Model):
    name = CharField()
    story = TextField()
    date = DateField()
    district = ForeignKeyField(District, related_name='stories')


def create_tables(fail_silently=False):
    models = database.Model.__subclasses__()
    create_model_tables(models, fail_silently=fail_silently)
