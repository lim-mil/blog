from typing import Union

from pydantic import Field

from schemas.base import BaseSchema, IdMixin, DateTimeMixin
from schemas.post_category import PostCategory


class PostStatus:
    DRAFT = 0
    PUBLISH = 1
    DELETE = -1


class PostBase(BaseSchema):
    title: str = Field(..., description='标题', max_length=32)
    content: str = Field(..., description='内容')
    status: int = Field(PostStatus.DRAFT, description='状态')


class Post(PostBase, IdMixin, DateTimeMixin):
    category_id: int = Field(..., description='分类外键')



class PostOut(PostBase, IdMixin, DateTimeMixin):
    category_id: Union[dict, int] = Field(..., description='分类')
