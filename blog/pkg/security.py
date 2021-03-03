import datetime
import traceback
from typing import Optional

import jwt
from fastapi import Header, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from blog.apps.oauth.models import OauthModel
from blog.apps.user.models import UserModel
from blog.apps.user.schemas import BaseUser
from blog.pkg.exception import BAD_REQUEST_400_Exception, FORBIDDEN_403_Exception, UNAUTHORIZED_401_Exception


oauth2_schema = OAuth2PasswordBearer(tokenUrl='/api/v1/user/token')


SALT = 'blogsecret'


def create_jwt_token(user: BaseUser):
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }

    payload = {
        'username': user.username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }

    result = jwt.encode(payload=payload, key=SALT, algorithm='HS256', headers=headers)
    return result


def get_current_user(
    token: str = Depends(oauth2_schema)
):
    try:
        payload = jwt.decode(token, key=SALT, algorithms=['HS256'])
        if payload.get('username'):
            user = UserModel.get_or_none(UserModel.username == payload['username'])
            if user:
                return user
        if payload.get('login'):
            oauth = OauthModel.get_or_none(OauthModel.login == payload.get('login'))
            if oauth:
                return oauth
        raise UNAUTHORIZED_401_Exception()
    except jwt.ExpiredSignatureError:
        raise UNAUTHORIZED_401_Exception('jwt token 超时')
    except Exception as e:
        traceback.print_exc()


def create_oauth_jwt_token(oauth: OauthModel):
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }

    payload = {
        'login': oauth.login,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }

    result = jwt.encode(payload=payload, key=SALT, algorithm='HS256', headers=headers)
    return result


if __name__ == '__main__':
    a = create_jwt_token()
    print(a)