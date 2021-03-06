from fastapi import APIRouter

from blog.apps.post.router import router as post_router
from blog.apps.project.router import router as project_router
from blog.apps.info.router import router as info_router
from blog.apps.user.router import router as user_router
from blog.apps.oauth.router import router as oauth_router
from blog.apps.comment.router import router as comment_router


api_v1 = APIRouter()


api_v1.include_router(
    router=post_router,
    prefix='/posts',
    tags=['posts'],
)

api_v1.include_router(
    router=project_router,
    prefix='/projects',
    tags=['projects']
)

api_v1.include_router(
    router=info_router,
    prefix='/info',
    tags=['info']
)

api_v1.include_router(
    router=user_router,
    prefix='/users',
    tags=['users']
)

api_v1.include_router(
    router=oauth_router,
    prefix='/oauth',
    tags=['oauth']
)

api_v1.include_router(
    router=comment_router,
    prefix='/comments',
    tags=['comments']
)