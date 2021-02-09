from peewee import SqliteDatabase

from blog import settings


sqlite_db = SqliteDatabase(settings.SQLITE_PATH)


def sqlite_connect():
    from blog.apps.info.models import InfoModel, BlogrolModel
    from blog.apps.post.models import PostModel, PostCategoryModel
    from blog.apps.project.model import ProjectModel, ProjectCategoryModel
    from blog.apps.user.models import UserModel


    sqlite_db.connect()
    sqlite_db.create_tables([PostModel, PostCategoryModel, ProjectModel, ProjectCategoryModel, InfoModel, BlogrolModel, UserModel])
