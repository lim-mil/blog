from blog.db.databases import sqlite_db
from blog.info.models import InfoModel, BlogrolModel
from blog.post.models import PostModel, PostCategoryModel
from blog.project.model import ProjectModel, ProjectCategoryModel


def sqlite_connect():
    sqlite_db.connect()
    sqlite_db.create_tables([PostModel, PostCategoryModel, ProjectModel, ProjectCategoryModel, InfoModel, BlogrolModel])
