from datetime import datetime

from peewee import Model, AutoField, BigIntegerField

from blog.pkg.db import sqlite_db
from blog.utils.get_current_ts import get_current_ts


class BaseModel(Model):
    id = AutoField(index=True, primary_key=True)
    created = BigIntegerField(default=get_current_ts)
    updated = BigIntegerField(default=get_current_ts)

    class Meta:
        database = sqlite_db
