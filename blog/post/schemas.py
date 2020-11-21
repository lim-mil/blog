from typing import Optional, List

from pydantic import Field

from schemas import BaseSchema, IdMixin, DatetimeMixin


class Post(BaseSchema):
    title: str = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)
    content: str
    status: int = Field(0)


class PostUpdate(BaseSchema):
    title: Optional[str] = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)
    content: Optional[str]
    status: Optional[int]


class PostCategory(BaseSchema):
    name: str = Field(..., max_length=64)


class PostIn(Post):
    category_id: int = Field(..., gt=0)


class PostCategoryIn(PostCategory):
    pass


class PostCategoryOut(PostCategory, IdMixin, DatetimeMixin):
    pass


class PostOut(Post, IdMixin, DatetimeMixin):
    category: Optional[PostCategoryOut]


class PostOutList(BaseSchema):
    post_list: List[PostOut] = Field([])


class PostCategoryList(BaseSchema):
    post_cateogry_list: List[PostCategoryOut] = Field([])
