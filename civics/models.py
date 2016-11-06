import json

from peewee import *
from peewee import create_model_tables
from playhouse.shortcuts import dict_to_model

from . import database


class Representative(database.Model):
    name = CharField()
    email = CharField()


class District(database.Model):
    ocd = CharField(unique=True)
    name = CharField()
    representative = ForeignKeyField(Representative, related_name='district', unique=True, null=True)


class Story(database.Model):
    name = CharField()
    story = TextField()
    date = DateField()
    district = ForeignKeyField(District, related_name='stories')


def create_tables(fail_silently=False):
    models = database.Model.__subclasses__()
    create_model_tables(models, fail_silently=fail_silently)


def load_json(filename):
    pairs = [("representatives", Representative),
             ("districts", District),
             ("stories", Story)]
    with open(filename, 'r') as f:
        data = json.load(f)
        for (name, model) in pairs:
            try:
                for row in data[name]:
                    m = dict_to_model(model, row)
                    m.save()
            except Exception as e:
                print("Error loading data from section: %s" % name)
                print(str(e))
