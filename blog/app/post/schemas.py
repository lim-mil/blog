from typing import Optional, List

from pydantic import Field

from blog.schemas import BaseSchema, IdMixin, DatetimeMixin, BaseResponse


class BasePost(BaseSchema):
    pass


class BasePostCategory(BaseSchema):
    name: str = Field(..., max_length=64)


class PostInCreate(BaseSchema):
    title: str = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)
    content: str
    status: int = Field(0)
    category_id: int = Field(..., gt=0)


class PostInUpdate(BaseSchema):
    title: Optional[str]
    desccription: Optional[str]
    content: Optional[str]
    status: Optional[int]


class PostCategoryInPost(BasePostCategory, IdMixin):
    pass


class PostInResponse(BaseSchema, IdMixin, DatetimeMixin):
    title: str = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)
    content: str
    status: int = Field(0)
    category: Optional[PostCategoryInPost]


class PostInListResponse(BaseSchema, IdMixin, DatetimeMixin):
    title: str = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)
    status: int = Field(0)
    category: Optional[PostCategoryInPost]


class PostInPostCategory(BaseSchema):
    title: str = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)


class PostCategoryInResponse(BaseSchema, IdMixin, DatetimeMixin):
    name: str = Field(..., max_length=64)
    posts: List[PostInPostCategory] = []


class PostCategoriesForResponse(BaseResponse):
    data: List[PostCategoryInResponse] = []


class PostCategoryForResponse(BaseResponse):
    data: Optional[PostCategoryInResponse]


class PostForResponse(BaseResponse):
    data: Optional[PostInResponse]


class PostsForResponse(BaseResponse):
    data: List[PostInListResponse] = []
