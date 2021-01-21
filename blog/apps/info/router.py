from typing import List

from fastapi import APIRouter

from blog.apps.info import crud
from blog.apps.info.schemas import InfoInCreate, InfoForResponse, AboutForResponse, BaseBlogrol, BlogrolsForResponse
from blog.pkg.response import resp_200

router = APIRouter()


@router.post(
    '/',
    description='',
    summary='创建个人信息'
)
async def create_info(
    info: InfoInCreate
):
    crud.create_info(info)
    return resp_200()


@router.get(
    '/',
    description='',
    summary='获取个人信息',
    response_model=InfoForResponse
)
async def retrive_info():
    info = crud.retrive_info()
    return InfoForResponse(data=info.dict())


@router.get(
    '/about',
    description='',
    summary='获取about',
    response_model=AboutForResponse
)
async def retrive_about():
    about = crud.retrive_about()
    return AboutForResponse(data=about.dict())


@router.post(
    '/blogrol',
    description='',
    summary='创建友链'
)
async def create_blogrol(
    blogrol: BaseBlogrol
):
    crud.create_blogrol(blogrol)
    return resp_200()


@router.get(
    '/blogrol',
    description='',
    summary='获取友链',
    response_model=BlogrolsForResponse,
)
async def list_blogrol():
    data = crud.list_blogrol()
    return BlogrolsForResponse(data=data)