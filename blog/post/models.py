from peewee import CharField, TextField, IntegerField

from models import BaseModel


POST_STATUS = {
    'draft': 0,
    'published': 1,
    'delete': 2
}


class PostModel(BaseModel):
    title = CharField(max_length=64, index=True, help_text='标题')
    description = CharField(max_length=256, index=True, help_text='描述')
    content = TextField(index=True, help_text='内容')
    status = IntegerField(default=0, choices=POST_STATUS)
    category_id = IntegerField(index=True)


class PostCategoryModel(BaseModel):
    name = CharField(max_length=64, index=True)
