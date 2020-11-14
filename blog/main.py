import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from routers import post


app = FastAPI()

app.include_router(
    post.router,
    prefix='/post'
)

if __name__ == '__main__':
    register_tortoise(app,
                      db_url='sqlite://db.sqlite3',
                      modules={'models': ['blog.models.post', 'blog.models.post_category']},
                      generate_schemas=True,
                      add_exception_handlers=True)
    uvicorn.run(app, )
