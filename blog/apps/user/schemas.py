from typing import Optional

from pydantic import Field

from blog.schemas import BaseSchema


class BaseUser(BaseSchema):
    username: str = Field(max_length=64)
    password: str = Field(max_length=512)


class UserInRegister(BaseUser):
    repassword: str = Field(max_length=512)


class UserInUpdate(BaseUser):
    username: Optional[str] = Field(max_length=64)
    password: Optional[str] = Field(max_length=512)
    repassword: Optional[str] = Field(max_length=512)
