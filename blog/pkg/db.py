from peewee import SqliteDatabase, MySQLDatabase
from playhouse.db_url import connect

from blog import settings


MYSQL_DB = connect(settings.MYSQL_URL, timeout=1800)


def create_tables():
    from blog.apps.info.models import InfoModel, BlogrolModel
    from blog.apps.post.models import PostModel, PostCategoryModel
    from blog.apps.project.model import ProjectModel, ProjectCategoryModel
    from blog.apps.user.models import UserModel
    from blog.apps.oauth.models import OauthModel
    from blog.apps.comment.models import CommentModel

    MYSQL_DB.create_tables([PostModel, PostCategoryModel, ProjectModel, ProjectCategoryModel, InfoModel, BlogrolModel,
                            UserModel, OauthModel, CommentModel])
