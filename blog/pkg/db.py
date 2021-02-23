from peewee import SqliteDatabase
from peewee_async import MySQLDatabase

from blog import settings


sqlite_db = SqliteDatabase(settings.SQLITE_PATH)
MYSQL_DB = MySQLDatabase(settings.DB_NAME, **{'charset': 'utf8', 'use_unicode': True, 'host': settings.DB_HOST, 'port': settings.DB_PORT,
                                        'user': settings.DB_USER, 'password': settings.DB_PASSWORD})


def sqlite_connect():
    from blog.apps.info.models import InfoModel, BlogrolModel
    from blog.apps.post.models import PostModel, PostCategoryModel
    from blog.apps.project.model import ProjectModel, ProjectCategoryModel
    from blog.apps.user.models import UserModel

    sqlite_db.create_tables([PostModel, PostCategoryModel, ProjectModel, ProjectCategoryModel, InfoModel, BlogrolModel, UserModel])
