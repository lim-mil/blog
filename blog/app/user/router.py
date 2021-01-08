from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from blog.app.user.schemas import UserIn, User
from blog.app.user import crud
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
        raise HTTPException(status_code=400, detail='不存在该用户')
    if not form_data.password == user.password:
        raise HTTPException(status_code=400, detail='密码错误')

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
