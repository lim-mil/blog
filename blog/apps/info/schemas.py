from typing import List, Optional

from pydantic import Field

from blog.schemas import BaseSchema, DatetimeMixin, BaseResponse


class BaseInfo(BaseSchema):
    name: str = Field('limyel', max_length=64)
    description: str = Field('Pythonista', max_length=256)
    location: str = Field('福州', max_length=64)
    job: str = Field('None', max_length=64)
    link: str = Field('https://github.com/lim-mil', max_length=512)


class BaseBlogrol(BaseSchema):
    name: str = Field(..., max_length=64)
    link: str = Field(..., max_length=64)


class AboutInResponse(BaseSchema):
    about: str = Field('')


class InfoInUpdate(BaseSchema):
    name: Optional[str]
    description: Optional[str]
    location: Optional[str]
    job: Optional[str]
    link: Optional[str]
    about: Optional[str]


class InfoInCreate(BaseInfo, AboutInResponse):
    pass


class InfoForResponse(BaseResponse):
    data: BaseInfo


class AboutForResponse(BaseResponse):
    data: AboutInResponse


class BlogrolsForResponse(BaseResponse):
    data: List[BaseBlogrol]