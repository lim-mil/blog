from peewee import Field, CharField

from blog.models import BaseModel


class OauthModel(BaseModel):
    login = CharField(max_length=256, index=True, help_text='用户名')
    avatar_url = CharField(max_length=1024, index=True, help_text='头像')
    html_url = CharField(max_length=1024, index=True, help_text='主页')
    email = CharField(max_length=128, null=True, index=True, help_text='邮箱')
