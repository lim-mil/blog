from pydantic import Field

from schemas.base import BaseSchema


class BlogRoll(BaseSchema):
    name: str = Field(..., max_length=32)
    link: str = Field(...)
