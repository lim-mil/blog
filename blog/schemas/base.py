from datetime import datetime

from pydantic import Field
from pydantic.main import Model


class BaseSchema(Model):
    id: str = Field(...)
    created: datetime = Field(..., default_factory=datetime.now, description='创建日期', )
    updated: datetime = Field(..., default_factory=datetime.now, description='更新日期')
