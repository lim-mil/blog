from typing import Optional, List, Any

from fastapi import APIRouter, Path, Query, Depends, Response, HTTPException
from fastapi.security import OAuth2PasswordBearer

from blog.apps.post import crud
from blog.apps.post.schemas import PostsForResponse, PostInResponse, BasePostCategory, PostInUpdate, \
    PostInCreate, PostCategoryForResponse, PostCategoriesForResponse, PostForResponse, PostCategoriesSimpleForResponse
from blog.apps.user.models import UserModel
from blog.pkg.security import oauth2_schema, get_current_user

router = APIRouter()


@router.post(
    '/',
    description='',
    summary='创建文章'
)
async def create_post(
    post: PostInCreate,
    user: UserModel = Depends(get_current_user)
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
):
    posts = crud.list_post(page, step)
    return PostsForResponse(data=posts)


@router.get(
    '/categories',
    description='',
    summary='所有分类',
    response_model=PostCategoriesForResponse,
)
async def list_post_category():
    print("ok")
    post_categories = crud.list_post_category()
    print(post_categories)
    return PostCategoriesForResponse(data=post_categories)


@router.get(
    '/{post_id}',
    response_model=PostForResponse,
    description='',
    summary='通过 id 获取文章'
)
async def retrive_post(
    post_id: int = Path(..., gt=0, description='文章 id'),
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
    user: UserModel = Depends(get_current_user)
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
    post_id: int = Path(..., gt=0, description='文章 id'),
    user: UserModel = Depends(get_current_user)
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
    post_category_id: int = Path(..., gt=0, description='分类 id'),
    user: UserModel = Depends(get_current_user)
):
    crud.delete_post_category_by_id(post_category_id)
    return {
        'status': 'ok'
    }


@router.patch(
    '/{post_id}',
    description='',
    summary='更改文章',
    response_model=PostForResponse
)
async def update_post(
    post: PostInUpdate,
    post_id: int = Path(..., gt=0, description='文章 id'),
    user: UserModel = Depends(get_current_user)
):
    data: PostInResponse = crud.update_post_by_id(post_id, post)
    return PostForResponse(data=data)


@router.patch(
    '/categories/{post_category_id}',
    description='',
    summary='更改分类',
    response_model=PostCategoryForResponse
)
async def update_post_category(
    post_category: BasePostCategory,
    post_category_id: int = Path(..., gt=0),
    user: UserModel = Depends(get_current_user)
):
    data = crud.update_post_category_by_id(post_category_id, post_category)
    return PostCategoryForResponse(data=data)


@router.get(
    '/categories/simple',
    description='',
    summary='获取所有分类（简单）',
    response_model=PostCategoriesSimpleForResponse
)
async def list_post_category_simple():
    data = crud.list_post_category_simple()
    return PostCategoriesSimpleForResponse(data=data)


@router.get(
    '/categories/{post_category_id}',
    description='',
    summary='获取分类（通过id）',
    response_model=PostCategoryForResponse
)
async def retrive_post_category(
    post_category_id: int = Path(..., gt=0),
):
    post_category = crud.retrive_post_category_by_id(post_category_id)
    return PostCategoryForResponse(data=post_category)
