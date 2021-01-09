from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from blog.app.user.schemas import UserIn, User
from blog.app.user import crud
from blog.pkg.exception import UNAUTHORIZED_401_Exception, FORBIDDEN_403_Exception
from blog.pkg.security import create_jwt_token

router = APIRouter()


@router.post(
    '/token',
    description='',
    summary='获取 jwt token',
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud.retrive_user_by_username(form_data.username)
    if not user:
        raise UNAUTHORIZED_401_Exception('用户名不存在')
    if not form_data.password == user.password:
        raise FORBIDDEN_403_Exception('密码错误')

    token = create_jwt_token()
    return {'access_token': token, 'token_type': 'bearer'}


@router.post(
    '/register',
    description='',
    summary='注册'
)
async def register(
    user: UserIn
):
    if user.password.strip() != user.repassword.strip():
        return
    crud.create_user(User(username=user.username, password=user.password))
    return {'status': 'ok'}
