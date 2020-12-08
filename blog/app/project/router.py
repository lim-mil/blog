from typing import List

from fastapi import APIRouter

from blog.app.project import crud
from blog.app.project import ProjectCategoryOut, ProjectIn, ProjectCategoryIn

router = APIRouter()


@router.get(
    '/categories',
    description='',
    summary='获取所有任务分类',
    response_model=List[ProjectCategoryOut]
)
async def list_project_category():
    return crud.list_project_category()


@router.post(
    '/',
    description='',
    summary='创建项目'
)
async def create_project(
    project: ProjectIn
):
    crud.create_project(project)
    return {
        'status': 'ok'
    }


@router.post(
    '/categories',
    description='',
    summary='创建分类'
)
async def create_category(
    project_category: ProjectCategoryIn
):
    crud.create_project_category(project_category)
    return {
        'status': 'ok'
    }
