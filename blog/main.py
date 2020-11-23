import uvicorn
from fastapi import FastAPI

from db.connetctions import sqlite_connect
from post.router import router as post_router
from project.router import router as project_router

app = FastAPI()


def start():
    sqlite_connect()
    app.include_router(
        router=post_router,
        prefix='/post',
        tags=['post'],
    )
    app.include_router(
        router=project_router,
        prefix='/project',
        tags=['project']
    )


if __name__ == '__main__':
    start()
    uvicorn.run(app, port=7331)
