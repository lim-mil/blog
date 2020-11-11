from pydantic import Field

from blog.schemas.base import BaseSchema


class PostCategory(BaseSchema):
    name: str = Field(..., max_length=32)
