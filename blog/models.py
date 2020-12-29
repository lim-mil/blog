from datetime import datetime

from peewee import Model, AutoField, DateTimeField, TimestampField

from blog.db.databases import sqlite_db


class BaseModel(Model):
    id = AutoField(index=True, primary_key=True)
    created = TimestampField(default=datetime.now)
    updated = TimestampField(default=datetime.now)

    class Meta:
        database = sqlite_db
