from datetime import datetime

import peewee_async
from peewee import Model, AutoField, BigIntegerField, DoesNotExist

from blog.pkg.db import sqlite_db, MYSQL_DB
from blog.utils.get_current_ts import get_current_ts


class BaseModel(Model):
    id = AutoField(index=True, primary_key=True)
    created = BigIntegerField(default=get_current_ts)
    updated = BigIntegerField(default=get_current_ts)

    class Meta:
        database = sqlite_db


class BaseManager:
    db = MYSQL_DB
    _manager = None

    def __init__(self):
        self._manager = peewee_async.Manager(self.db)

    @property
    def manager(self):
        return self._manager

    async def get_by_id(self, id: int):
        return await self._manager.get(self.model, id=id)

    async def create(self, **kwargs):
        return await self.create(self.model, **kwargs)

    async def get_or_none(self, **kwargs):
        try:
            return await self._manager.get(self.model, **kwargs)
        except DoesNotExist:
            return None
