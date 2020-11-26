from typing import Optional, List

from fastapi import APIRouter, Path, Query

from post import crud
from post.schemas import PostIn, PostOut, PostCategoryIn, PostOutList, PostUpdate, PostCategory, PostCategoryOut

router = APIRouter()


@router.post(
    '/',
    description='',
    summary='创建文章'
)
async def create_post(
    post: PostIn
):
    crud.create_post(post)
    return {
        'status': 'ok'
    }


@router.get(
    '/list',
    response_model=PostOutList,
    description='',
    summary='所有文章（分页）'
)
async def list_post(
    page: Optional[int] = Query(None, ge=1, description='页数，不传则默认获取全部'),
    step: Optional[int] = Query(None, ge=1, description='偏移，不传则默认获取全部')
):
    posts = crud.list_post(page, step)
    return posts


@router.get(
    '/{post_id}',
    response_model=PostOut,
    description='',
    summary='通过 id 获取文章'
)
async def retrive_post(
    post_id: int = Path(..., gt=0, description='文章 id')
):
    post_out = crud.retrive_post_by_id(post_id)
    return post_out


@router.post(
    '/categories',
    description='',
    summary='创建文章分类'
)
async def create_post_category(
    post_category: PostCategoryIn,
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
    post: PostUpdate,
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
    post_category: PostCategory,
    post_category_id: int = Path(..., gt=0)
):
    crud.update_post_category_by_id(post_category_id, post_category)
    return {
        'status': 'ok'
    }


@router.get(
    '/categories/',
    description='',
    summary='所有分类',
    response_model=List[PostCategoryOut],
)
async def list_post_category():
    return crud.list_post_category()