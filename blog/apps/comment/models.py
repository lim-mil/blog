from peewee import TextField, IntegerField

from blog.models import BaseModel


class CommentModel(BaseModel):
    content = TextField(help_text='评论内容')
    oauth_id = IntegerField(index=True, help_text='用户')
    post_id = IntegerField(index=True, help_text='文章')
    target_comment_id = IntegerField(index=True, help_text='目标评论')
    target_oauth_id = IntegerField(index=True, help_text='目标用户')
