from blog.apps.project.model import ProjectModel, ProjectCategoryModel
from blog.apps.user.models import UserModel
from blog.db.databases import sqlite_db
from blog.apps.info.models import InfoModel, BlogrolModel
from blog.apps.post.models import PostModel, PostCategoryModel


def sqlite_connect():
    sqlite_db.connect()
    sqlite_db.create_tables([PostModel, PostCategoryModel, ProjectModel, ProjectCategoryModel, InfoModel, BlogrolModel, UserModel])
