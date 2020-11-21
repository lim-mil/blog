from datetime import datetime

from peewee import Model, AutoField, DateTimeField

from db.databases import sqlite_db


class BaseModel(Model):
    id = AutoField(index=True, primary_key=True)
    created = DateTimeField(default=datetime.now)
    updated = DateTimeField(default=datetime.now)

    class Meta:
        database = sqlite_db
