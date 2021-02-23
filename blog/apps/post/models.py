from peewee import CharField, TextField, IntegerField

from blog.models import BaseModel, BaseManager


class POST_STATUS:
    draft = 0
    published = 1
    delete = 2


class PostModel(BaseModel):
    title = CharField(max_length=64, index=True, help_text='标题')
    description = CharField(max_length=256, index=True, help_text='描述')
    content = TextField(index=True, help_text='内容')
    status = IntegerField(default=POST_STATUS.draft)
    category_id = IntegerField(index=True)


class PostCategoryModel(BaseModel):
    name = CharField(max_length=64, index=True)

    @property
    def posts_set(self):
        posts = PostModel.select(PostModel.id).where(PostModel.category_id == self.id)
        return set(post.id for post in posts)


class PostModelManager(BaseManager):
    model = PostModel


post_model_manager = PostModelManager()


class PostCategoryModelManager(BaseManager):
    model = PostCategoryModel


post_category_model_manager = PostCategoryModelManager()
