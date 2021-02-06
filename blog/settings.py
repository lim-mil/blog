import os


BASE_DIR = os.path.dirname(__file__)
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

HOST = '127.0.0.1'
PORT = 7331

SECRET_KEY = 'secret_key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SQLITE_PATH = ''


try:
    if os.path.exists(os.path.join(os.path.dirname(__file__), 'private.py')):
        from private import *
except Exception as e:
    pass