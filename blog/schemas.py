from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, validator


class BaseSchema(BaseModel):
    pass

    class Config:
        orm_mode = True


class IdMixin(BaseModel):
    id: Optional[int]


class DatetimeMixin(BaseModel):
    created: Optional[datetime]
    updated: Optional[datetime]

    @validator('created', 'updated')
    def created_dt2ts(cls, v):
        if not isinstance(v, datetime):
            raise ValueError('must be datetime instance')
        return v.timestamp()
