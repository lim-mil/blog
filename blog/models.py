from datetime import datetime

import peewee_async
from peewee import Model, AutoField, BigIntegerField, DoesNotExist

from blog.pkg.db import MYSQL_DB
from blog.utils.get_current_ts import get_current_ts


class BaseModel(Model):
    id = AutoField(index=True, primary_key=True)
    created = BigIntegerField(default=get_current_ts)
    updated = BigIntegerField(default=get_current_ts)

    class Meta:
        database = MYSQL_DB
