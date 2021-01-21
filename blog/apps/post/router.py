from typing import Optional, List, Any

from fastapi import APIRouter, Path, Query, Depends, Response, HTTPException
from fastapi.security import OAuth2PasswordBearer

from blog.apps.post import crud
from blog.apps.post.schemas import PostsForResponse, PostInResponse, BasePostCategory, PostInUpdate, \
    PostInCreate, PostCategoryForResponse, PostCategoriesForResponse, PostForResponse
from blog.pkg.security import oauth2_schema, get_current_user

router = APIRouter()


@router.post(
    '/',
    description='',
    summary='创建文章'
)
async def create_post(
    post: PostInCreate
):
    crud.create_post(post)
    return {
        'status': 'ok'
    }


@router.get(
    '/',
    response_model=PostsForResponse,
    response_model_by_alias='data',
    description='',
    summary='所有文章（分页）'
)
async def list_post(
    page: Optional[int] = Query(None, ge=1, description='页数，不传则默认获取全部'),
    step: Optional[int] = Query(None, ge=1, description='偏移，不传则默认获取全部'),
    user: Any = Depends(get_current_user),
):
    posts = crud.list_post(page, step)
    return PostsForResponse(data=posts)


@router.get(
    '/{post_id}',
    response_model=PostForResponse,
    description='',
    summary='通过 id 获取文章'
)
async def retrive_post(
    post_id: int = Path(..., gt=0, description='文章 id')
):
    post = crud.retrive_post_by_id(post_id)
    return PostForResponse(data=post.dict())


@router.post(
    '/categories',
    description='',
    summary='创建文章分类'
)
async def create_post_category(
    post_category: BasePostCategory,
):
    crud.create_post_category(post_category)
    return {
        'status': 'ok'
    }


@router.delete(
    '/{post_id}',
    description='',
    summary='删除文章（id）'
)
async def delete_post(
    post_id: int = Path(..., gt=0, description='文章 id')
):
    crud.delete_post_by_id(post_id)
    return {
        'status': 'ok'
    }


@router.delete(
    '/categories/{post_category_id}',
    description='',
    summary='删除文章分类（id）'
)
async def delete_post_category(
    post_category_id: int = Path(..., gt=0, description='分类 id')
):
    crud.delete_post_category_by_id(post_category_id)
    return {
        'status': 'ok'
    }


@router.patch(
    '/{post_id}',
    description='',
    summary='更改文章'
)
async def update_post(
    post: PostInUpdate,
    post_id: int = Path(..., gt=0, description='文章 id')
):
    crud.update_post_by_id(post_id, post)
    return {
        'status': 'ok'
    }


@router.patch(
    '/categories/{post_category_id}',
    description='',
    summary='更改分类'
)
async def update_post_category(
    post_category: BasePostCategory,
    post_category_id: int = Path(..., gt=0)
):
    crud.update_post_category_by_id(post_category_id, post_category)


@router.get(
    '/categories/',
    description='',
    summary='所有分类',
    response_model=PostCategoriesForResponse,
)
async def list_post_category():
    post_categories = crud.list_post_category()
    return PostCategoriesForResponse(data=post_categories)


@router.get(
    '/category/{post_category_id}',
    description='',
    summary='获取分类（通过id）',
    response_model=PostCategoryForResponse
)
async def retrive_post_category(
    post_category_id: int = Path(..., gt=0)
):
    post_category = crud.retrive_post_category_by_id(post_category_id)
    return PostCategoryForResponse(data=post_category)
