from peewee import CharField, IntegerField

from models import BaseModel


PROJECT_STATUS = {
    'doing': 0,
    'stop': 1,
    'delete': -1
}


class ProjectModel(BaseModel):
    name = CharField(max_length=64, index=True)
    description = CharField(max_length=128, index=True, help_text='描述')
    link = CharField(max_length=512, index=True, help_text='项目地址')
    status = IntegerField(default=0, choices=PROJECT_STATUS)
    category_id = IntegerField(index=True)


class ProjectCategoryModel(BaseModel):
    name = CharField(max_length=64, index=True)
