from typing import Optional, List

from pydantic import Field

from blog.schemas import BaseSchema, IdMixin, DatetimeMixin


class Project(BaseSchema):
    name: str = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)
    link: str = Field(..., max_length=512)
    status: int = Field(0, description='项目状态，0：正常，1：停止，-1：删除')


class ProjectCategory(BaseSchema):
    name: str = Field(..., max_length=64)


class ProjectIn(Project):
    category_id: int = Field(..., gt=0)


class ProjectOut(Project, IdMixin, DatetimeMixin):
    category: ProjectCategory


class ProjectCategoryIn(ProjectCategory):
    pass


class CategoryProjectOut(Project, IdMixin, DatetimeMixin):
    pass


class ProjectCategoryOut(ProjectCategory, IdMixin, DatetimeMixin):
    projects: Optional[List[CategoryProjectOut]]


class ProjectUpdate(BaseSchema):
    name: Optional[str] = Field(..., max_length=64)
    description: Optional[str] = Field(..., max_length=128)
    link: Optional[str] = Field(..., max_length=512)
    status: Optional[int] = Field(0, description='项目状态，0：正常，1：停止，-1：删除')
    category_id: Optional[int] = Field(..., gt=0)
