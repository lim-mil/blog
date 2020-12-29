import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from blog.app.api import api_v1
from blog.db.connetctions import sqlite_connect


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

# 静态资源
app.mount('/static', StaticFiles(directory='static'), name='static')


def start():
    sqlite_connect()
    app.include_router(
        router=api_v1,
        prefix='/api/v1'
    )


if __name__ == '__main__':
    start()
    uvicorn.run(app, port=7331)
