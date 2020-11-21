from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseSchema(BaseModel):
    pass

    class Config:
        orm_mode = True


class IdMixin(BaseModel):
    id: Optional[int]


class DatetimeMixin(BaseModel):
    created: Optional[datetime]
    updated: Optional[datetime]
