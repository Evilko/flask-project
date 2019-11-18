import datetime
from peewee import *
from app import db


class Note(db.Model):
    title = CharField(max_length=100)
    message = TextField()
    created = DateTimeField(default=datetime.datetime.now)
