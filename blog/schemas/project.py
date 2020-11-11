from pydantic import Field

from blog.schemas.base import BaseSchema


class ProjectStatus:
    STOP: int = 0
    DOING: int = 1


class Project(BaseSchema):
    name: str = Field(..., max_length=32, description='项目名')
    description: str = Field(..., max_length=64, description='描述')
    link: str = Field(..., regex=None, description='项目地址')
    status: int = Field(...)
    category_id: int = Field(...)
