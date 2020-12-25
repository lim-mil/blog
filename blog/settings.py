import os


SECRET_KEY = 'secret_key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


private_path = os.path.join(os.path.dirname(__file__))
