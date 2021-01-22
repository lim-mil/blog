from typing import Optional, List

from pydantic import Field

from blog.schemas import BaseSchema, IdMixin, DatetimeMixin, BaseResponse


class BaseProject(BaseSchema):
    name: str = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)
    link: str = Field(..., max_length=512)
    status: int = Field(0, description='项目状态，0：正常，1：停止，-1：删除')


class BaseProjectCategory(BaseSchema):
    name: str = Field(..., max_length=64)


class ProjectInCreate(BaseProject):
    category_id: int = Field(..., gt=0)


class ProjectInUpdate(BaseSchema):
    name: Optional[str]
    description: Optional[str]
    link: Optional[str]
    status: Optional[int]
    category_id: Optional[int]


class ProjectCategoryInProject(BaseProjectCategory, IdMixin):
    pass


class ProjectInResponse(BaseProject, IdMixin, DatetimeMixin):
    category: Optional[ProjectCategoryInProject]


class ProjectUpdate(BaseSchema):
    name: Optional[str] = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)
    link: Optional[str] = Field(..., max_length=512)
    status: Optional[int] = Field(0, description='项目状态，0：正常，1：停止，-1：删除')
    category_id: Optional[int] = Field(..., gt=0)


class ProjectForResponse(BaseResponse):
    data: ProjectInResponse


class ProjectInProjectCategory(BaseProject, IdMixin):
    pass


class ProjectCategoryInResponse(BaseProjectCategory, IdMixin, DatetimeMixin):
    projects: List[ProjectInProjectCategory] = []


class ProjectCategoryForResponse(BaseResponse):
    data: ProjectInResponse


class ProjectCategoriesForResponse(BaseResponse):
    data: List[ProjectCategoryInResponse]
