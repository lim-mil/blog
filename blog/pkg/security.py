import datetime
from typing import Optional

import jwt
from fastapi import Header, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from blog.app.user.models import UserModel
from blog.pkg.exception import BAD_REQUEST_400_Exception, FORBIDDEN_403_Exception

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/api/v1/user/token')


SALT = 'blogsecret'


def create_jwt_token():
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }

    payload = {
        'user_id': 1,
        'username': 'test',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=3)
    }

    result = jwt.encode(payload=payload, key=SALT, algorithm='HS256', headers=headers).encode('utf-8')
    return result


def check_jwt_token(
        token: Optional[str] = Header(None)
):
    try:
        result = jwt.decode(token, key=SALT, algorithms=['HS256'])
        return result
    except Exception as e:
        pass


def get_current_user(
    token: str = Depends(oauth2_schema)
):
    try:
        payload = jwt.decode(token, key=SALT, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise FORBIDDEN_403_Exception()
    except (jwt.PyJWTError, AttributeError):
        import traceback
        traceback.print_exc()
        raise HTTPException

    user = UserModel.get_or_none(UserModel.username == payload['username'])
    if user:
        return user
    else:
        raise Exception('error')


if __name__ == '__main__':
    a = create_jwt_token()
    print(a)