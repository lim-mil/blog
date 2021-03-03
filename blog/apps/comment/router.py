from fastapi import APIRouter, Path, Depends

from blog.apps.comment import crud
from blog.apps.comment.schemas import CommentForResponse, CommentInCreate
from blog.apps.oauth.models import OauthModel
from blog.pkg.response import resp_200
from blog.pkg.security import get_current_user

router = APIRouter()


@router.get(
    '/post/{post_id}',
    description='',
    summary='通过文章获取评论',
    response_model=CommentForResponse
)
async def comments_list(
    post_id: int = Path(..., gt=0, description='文章id')
):
    data = crud.retrive_comments_by_post_id(post_id)
    return CommentForResponse(data=data)


@router.post(
    '',
    description='',
    summary='创建评论'
)
async def create_comment(
    comment: CommentInCreate,
    oauth: OauthModel = Depends(get_current_user)
):
    crud.create_comment(comment)
    return resp_200()
