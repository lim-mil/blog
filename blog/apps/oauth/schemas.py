from typing import Optional

from blog.schemas import BaseSchema, BaseResponse, IdMixin


class OauthInResponse(BaseSchema, IdMixin):
    login: str
    avatar_url: str
    html_url: str
    email: Optional[str]


class OauthForResponse(BaseResponse):
    data: OauthInResponse
