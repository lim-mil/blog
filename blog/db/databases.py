from playhouse.db_url import SqliteDatabase, PostgresqlDatabase

from blog import settings

sqlite_db = SqliteDatabase(settings.SQLITE_PATH)

# postgresql_db = PostgresqlDatabase()