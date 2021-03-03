import json

import httpx
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from httpx import AsyncClient

from blog.apps.user.models import UserModel
from blog.apps.user.schemas import UserInRegister, BaseUser
from blog.apps.user import crud
from blog.pkg.exception import UNAUTHORIZED_401_Exception, FORBIDDEN_403_Exception, BAD_REQUEST_400_Exception
from blog.pkg.response import resp_200
from blog.pkg.security import create_jwt_token, get_current_user

router = APIRouter()


@router.post(
    '/token',
    description='',
    summary='获取 jwt token',
)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = crud.retrive_user_by_username(form_data.username)
    if not user:
        raise UNAUTHORIZED_401_Exception('用户名不存在')
    if not form_data.password == user.password:
        raise UNAUTHORIZED_401_Exception('密码错误')

    token = create_jwt_token(user)
    return resp_200(data={'access_token': token, 'token_type': 'bearer', 'username': user.username})


@router.post(
    '/register',
    description='',
    summary='注册'
)
async def register(
    user: UserInRegister
):
    if user.password.strip() != user.repassword.strip():
        raise BAD_REQUEST_400_Exception(msg="password is different from repassword.")
    crud.create_user(BaseUser(username=user.username, password=user.password))
    return resp_200()
