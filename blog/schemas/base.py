from datetime import datetime
from typing import Optional

from pydantic import Field
from pydantic import BaseModel


class BaseSchema(BaseModel):
    pass


class IdMixin(BaseModel):
    id: int = Field(...)


class DateTimeMixin(BaseModel):
    created: datetime = Field(default_factory=datetime.now)
    updated: datetime = Field(default_factory=datetime.now)
