import os


SECRET_KEY = 'secret_key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SQLITE_PATH = ''


try:
    if os.path.exists(os.path.join(os.path.dirname(__file__), 'private.py')):
        from private import *
except Exception as e:
    pass