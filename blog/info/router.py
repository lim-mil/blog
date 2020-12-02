from fastapi import APIRouter

from blog.info import crud
from blog.info.schemas import InfoIn, InfoOut, AboutOut, BlogrolIn, BlogrolList

router = APIRouter()


@router.post(
    '/',
    description='',
    summary='创建个人信息'
)
async def create_info(
    info: InfoIn
):
    crud.create_info(info)
    return {
        'status': 'ok'
    }


@router.get(
    '/',
    description='',
    summary='获取个人信息',
    response_model=InfoOut
)
async def retrive_info():
    info = crud.retrive_info()
    return info.dict()


@router.get(
    '/about',
    description='',
    summary='获取about',
    response_model=AboutOut
)
async def retrive_about():
    about = crud.retrive_about()
    return about.dict()


@router.post(
    '/blogrol',
    description='',
    summary='创建友链'
)
async def create_blogrol(
    blogrol: BlogrolIn
):
    crud.create_blogrol(blogrol)
    return {
        'status': 'ok'
    }


@router.get(
    '/blogrol',
    description='',
    summary='获取友链',
    response_model=BlogrolList
)
async def list_blogrol():
    return crud.list_blogrol().dict()
