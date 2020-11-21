import uvicorn
from fastapi import FastAPI

from db.connetctions import sqlite_connect
from post.router import router

app = FastAPI()
app.include_router(
    router=router,
    prefix='/post',
    tags=['post'],
)


def start():
    sqlite_connect()


if __name__ == '__main__':
    start()
    uvicorn.run(app, port=7331)
