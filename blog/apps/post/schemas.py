from typing import Optional, List

from pydantic import Field

from blog.schemas import BaseSchema, IdMixin, DatetimeMixin, BaseResponse


class BasePost(BaseSchema):
    """基础文章
    """
    title: str = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)
    content: str
    status: int = Field(0)


class BasePostCategory(BaseSchema):
    """基础文章分类
    """
    name: str = Field(..., max_length=64)


class PostInCreate(BasePost):
    """创建文章
    """
    category_id: int = Field(..., gt=0)


class PostInUpdate(BaseSchema):
    """更新文章
    """
    title: Optional[str]
    description: Optional[str]
    content: Optional[str]
    status: Optional[int]
    category_id: Optional[int]


class PostCategoryInPost(BasePostCategory, IdMixin):
    """文章中的的分类信息
    """
    pass


class PostInResponse(BasePost, IdMixin, DatetimeMixin):
    """完整的单篇文章
    """
    category: Optional[PostCategoryInPost]


class PostsInResponse(BaseSchema, IdMixin, DatetimeMixin):
    """获取多篇文章时的单个文章数据，用于首页等
    """
    title: str = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)
    status: int = Field(0)
    category: Optional[PostCategoryInPost]


class PostInPostCategory(BaseSchema, IdMixin, DatetimeMixin):
    """分类中展示的文章
    """
    title: str = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)


class PostCategoryInResponse(BasePostCategory, IdMixin, DatetimeMixin):
    """完整的单个分类
    """
    posts: List[PostInPostCategory] = []


class PostCategorySimpleInResponse(BasePostCategory, IdMixin):
    """简单的单个分类，用于修改文章等
    """
    pass


class PostCategoriesSimpleForResponse(BaseResponse):
    data: List[PostCategorySimpleInResponse] = []


class PostCategoriesForResponse(BaseResponse):
    data: List[PostCategoryInResponse] = []


class PostCategoryForResponse(BaseResponse):
    data: Optional[PostCategoryInResponse]


class PostForResponse(BaseResponse):
    data: Optional[PostInResponse]


class PostsForResponse(BaseResponse):
    data: List[PostsInResponse] = []


class PostCategoryForResponse(BaseResponse):
    data: PostCategoryInResponse
