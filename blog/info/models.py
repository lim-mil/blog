from peewee import CharField, TextField

from blog.models import BaseModel


class InfoModel(BaseModel):
    name = CharField(max_length=64, index=True)
    description = CharField(max_length=256, index=True)
    location = CharField(max_length=64, index=True)
    job = CharField(max_length=64, index=True)
    about = TextField(index=True)
    link = CharField(max_length=512, index=True)


class BlogrolModel(BaseModel):
    name = CharField(max_length=64, index=True)
    link = CharField(max_length=512, index=True)
