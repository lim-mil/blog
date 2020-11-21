from db.databases import sqlite_db
from post.models import PostModel, PostCategoryModel
from project.model import ProjectModel, ProjectCategoryModel


def sqlite_connect():
    sqlite_db.connect()
    sqlite_db.create_tables([PostModel, PostCategoryModel, ProjectModel, ProjectCategoryModel])
