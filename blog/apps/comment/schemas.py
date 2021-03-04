from typing import Optional, List

from blog.apps.oauth.schemas import OauthInResponse
from blog.schemas import BaseSchema, DatetimeMixin, IdMixin, BaseResponse


class CommentInResponse(BaseSchema, IdMixin, DatetimeMixin):
    content: str
    oauth: Optional[OauthInResponse]
    target_oauth: Optional[OauthInResponse]


class CommentInCreate(BaseSchema):
    content: str
    oauth_id: int
    post_id: int
    target_oauth_id: Optional[int]


class CommentForResponse(BaseResponse):
    data: List[CommentInResponse]
