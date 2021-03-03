from typing import List

from blog.apps.comment.models import CommentModel
from blog.apps.comment.schemas import CommentInResponse, CommentInCreate
from blog.apps.oauth.models import OauthModel
from blog.apps.oauth.schemas import OauthInResponse


def retrive_comments_by_post_id(id: int) -> List[CommentInResponse]:
    comments_model = CommentModel.select().where(CommentModel.post_id==id)
    result = []
    for comment_model in comments_model:
        comment_model: CommentModel
        comment = CommentInResponse.from_orm(comment_model)
        comment.oauth = OauthInResponse.from_orm(OauthModel.get_by_id(comment_model.oauth_id))
        comment.target_oauth = OauthInResponse.from_orm(OauthModel.get_by_id(comment_model.target_oauth_id))
        result.append(comment)
    return result


def create_comment(comment: CommentInCreate):
    CommentModel.create(**comment.dict())
