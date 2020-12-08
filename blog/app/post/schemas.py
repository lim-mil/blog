from typing import Optional, List

from pydantic import Field

from blog.schemas import BaseSchema, IdMixin, DatetimeMixin


class Post(BaseSchema):
    """
    文章
    """
    title: str = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)
    content: str
    status: int = Field(0)


class PostUpdate(BaseSchema):
    """
    更新文章
    """
    title: Optional[str] = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)
    content: Optional[str]
    status: Optional[int]


class PostCategory(BaseSchema):
    """
    文章分类
    """
    name: str = Field(..., max_length=64)


class PostIn(Post):
    """
    文章输入类
    """
    category_id: int = Field(..., gt=0)


class PostCategoryIn(PostCategory):
    pass


class CategoryPostOut(BaseSchema, IdMixin, DatetimeMixin):
    title: str = Field(..., max_length=64)


class PostCategoryOut(PostCategory, IdMixin, DatetimeMixin):
    posts: Optional[List[CategoryPostOut]]


class PostOut(Post, IdMixin, DatetimeMixin):
    category: Optional[PostCategoryOut]


class PostOutListItem(BaseSchema, IdMixin, DatetimeMixin):
    title: str = Field(..., max_length=64)
    description: str = Field(..., max_length=128)
    category: Optional[PostCategoryOut]


class PostOutList(BaseSchema):
    post_list: List[PostOutListItem] = Field([])

