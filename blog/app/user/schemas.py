from typing import Optional

from pydantic import Field

from blog.schemas import BaseSchema


class User(BaseSchema):
    username: str = Field(max_length=64)
    password: str = Field(max_length=512)


class UserIn(User):
    repassword: str = Field(max_length=512)


class UserOut(BaseSchema):
    username: str = Field(max_length=64)


class UserUpdate(BaseSchema):
    username: Optional[str] = Field(max_length=64)
    password: Optional[str] = Field(max_length=512)
    repassword: Optional[str] = Field(max_length=512)
