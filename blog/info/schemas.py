from typing import List, Optional

from pydantic import Field

from blog.schemas import BaseSchema, DatetimeMixin


class InfoOut(BaseSchema):
    name: str = Field(..., max_length=64)
    description: str = Field(..., max_length=256)
    location: str = Field(..., max_length=64)
    job: str = Field(..., max_length=64)


class AboutOut(BaseSchema):
    about: str


class InfoIn(InfoOut, AboutOut):
    pass


class Blogrol(BaseSchema):
    name: str = Field(..., max_length=64)
    link: str = Field(..., max_length=64)


class BlogrolList(BaseSchema):
    blogrols: Optional[List[Blogrol]]


class BlogrolIn(Blogrol):
    pass