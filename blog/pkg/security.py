from fastapi.security import OAuth2PasswordBearer


oauth2_schema = OAuth2PasswordBearer(tokenUrl='/api/v1/user/login')
