from typing import Optional, List

from pydantic import Field

from blog.schemas import BaseSchema, IdMixin, DatetimeMixin, BaseResponse


class BasePost(BaseSchema):
    title: str = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)
    content: str
    status: int = Field(0)


class BasePostCategory(BaseSchema):
    name: str = Field(..., max_length=64)


class PostInCreate(BasePost):
    category_id: int = Field(..., gt=0)


class PostInUpdate(BaseSchema):
    title: Optional[str]
    desccription: Optional[str]
    content: Optional[str]
    status: Optional[int]
    category_id: Optional[int]


class PostCategoryInPost(BasePostCategory, IdMixin):
    pass


class PostInResponse(BasePost, IdMixin, DatetimeMixin):
    category: Optional[PostCategoryInPost]


class PostInListResponse(BaseSchema, IdMixin, DatetimeMixin):
    title: str = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)
    status: int = Field(0)
    category: Optional[PostCategoryInPost]


class PostInPostCategory(BaseSchema, IdMixin, DatetimeMixin):
    title: str = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)


class PostCategoryInResponse(BasePostCategory, IdMixin, DatetimeMixin):
    posts: List[PostInPostCategory] = []


class PostCategoriesForResponse(BaseResponse):
    data: List[PostCategoryInResponse] = []


class PostCategoryForResponse(BaseResponse):
    data: Optional[PostCategoryInResponse]


class PostForResponse(BaseResponse):
    data: Optional[PostInResponse]


class PostsForResponse(BaseResponse):
    data: List[PostInListResponse] = []
