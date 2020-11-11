from pydantic import Field

from blog.schemas.base import BaseSchema


class PostStatus:
    DRAFT = 0
    PUBLISH = 1
    DELETE = -1


class Post(BaseSchema):
    title: str = Field(..., description='标题', max_length=32)
    content: str = Field(..., description='内容')
    status: int = Field(..., description='状态')
    category_id: int = Field(..., description='分类')
