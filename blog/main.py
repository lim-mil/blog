import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request

from blog.apps.api import api_v1
from blog.apps.exception_handler import register_exception_handlers
from blog.pkg.db import sqlite_connect
from blog.pkg.exception import FORBIDDEN_403_Exception
from blog.pkg.response import resp_403
from blog.settings import HOST, PORT

app = FastAPI()

origins = [
    "*"
]

# 跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 动态资源
app.mount('/media', StaticFiles(directory='media'), name='media')
# 静态资源
app.mount('/static', StaticFiles(directory='static'), name='static')


# @app.exception_handler(FORBIDDEN_403_Exception)
# async def forbidden_exception_handler(request: Request, exc: RequestValidationError):
#     return resp_403()
def start():
    sqlite_connect()
    app.include_router(
        router=api_v1,
        prefix='/api/v1'
    )
    register_exception_handlers(app)


if __name__ == '__main__':
    start()
    uvicorn.run(app, host=HOST, port=PORT)
