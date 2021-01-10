import datetime
import traceback
from typing import Optional

import jwt
from fastapi import Header, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from blog.app.user.models import UserModel
from blog.app.user.schemas import User
from blog.pkg.exception import BAD_REQUEST_400_Exception, FORBIDDEN_403_Exception, UNAUTHORIZED_401_Exception

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/api/v1/user/token')


SALT = 'blogsecret'


def create_jwt_token(user: User):
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }

    payload = {
        'username': user.username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=3)
    }

    result = jwt.encode(payload=payload, key=SALT, algorithm='HS256', headers=headers).encode('utf-8')
    return result


def get_current_user(
    token: str = Depends(oauth2_schema)
):
    try:
        payload = jwt.decode(token, key=SALT, algorithms=['HS256'])
        user = UserModel.get_or_none(UserModel.username == payload['username'])
        if user:
            return user
        else:
            raise UNAUTHORIZED_401_Exception()
    except jwt.ExpiredSignatureError:
        raise FORBIDDEN_403_Exception('jwt token 超时')
    except Exception as e:
        traceback.print_exc()


if __name__ == '__main__':
    a = create_jwt_token()
    print(a)