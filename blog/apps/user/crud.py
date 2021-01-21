from typing import Optional

from blog.apps.user.models import UserModel
from blog.apps.user.schemas import BaseUser, UserInUpdate


def create_user(user: BaseUser):
    result = UserModel.create(**user.dict())
    return result


def retrive_user_by_username(username: str) -> Optional[BaseUser]:
    user: Optional[UserModel] = UserModel.get_or_none(UserModel.username == username)
    if user:
        result = BaseUser.from_orm(user)
    else:
        result = None
    return result


def delete_user_by_id(id: int):
    row = UserModel.delete_by_id(id)
    return row


def retrive_user(username: str, password: str):
    user: Optional[UserModel] = UserModel.get_or_none(UserModel.username == username, UserModel.password == password)
    return user


def update_user(id: int, data: UserInUpdate):
    user: Optional[UserModel] = UserModel.get_by_id(id)
    if user:
        user.update(**data.dict())
        return user
    return None
