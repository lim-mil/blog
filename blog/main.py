import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from blog.db.connetctions import sqlite_connect
from blog.post.router import router as post_router
from blog.project.router import router as project_router
from blog.info.router import router as info_router


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/static', StaticFiles(directory='static'), name='static')


def start():
    sqlite_connect()
    app.include_router(
        router=post_router,
        prefix='/posts',
        tags=['posts'],
    )
    app.include_router(
        router=project_router,
        prefix='/projects',
        tags=['projects']
    )
    app.include_router(
        router=info_router,
        prefix='/info',
        tags=['info']
    )


if __name__ == '__main__':
    start()
    uvicorn.run(app, port=7331)
