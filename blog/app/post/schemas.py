from typing import Optional, List

from pydantic import Field

from blog.schemas import BaseSchema, IdMixin, DatetimeMixin, BaseResponse


class PostCreate(BaseSchema):
    title: str = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)
    content: str
    status: int = Field(0)
    category_id: int = Field(..., gt=0)


class PostUpdate(BaseSchema):
    title: str = Field(..., max_length=64)
    desccription: Optional[str] = Field(..., max_length=128)
    content: Optional[str]
    status: Optional[int]


class PostRetrive(BaseSchema, IdMixin, DatetimeMixin):
    title: str = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)
    content: str
    status: int = Field(0)
    category:


class PostCategoryCreate(BaseSchema):
    name: str = Field(..., max_length=64)


class




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


class PostsOut(BaseSchema):
    posts: List[PostOutListItem] = Field([])


class PostResponse(BaseResponse):
    data: PostOut


class PostsResponse(BaseResponse):
    data: PostsOut