from typing import List

from fastapi import APIRouter

from blog.apps.project import crud
from blog.apps.project.schemas import ProjectCategoriesForResponse, ProjectInCreate, BaseProjectCategory

router = APIRouter()


@router.get(
    '/categories',
    description='',
    summary='获取所有任务分类',
    response_model=ProjectCategoriesForResponse
)
async def list_project_category():
    return crud.list_project_category()


@router.post(
    '/',
    description='',
    summary='创建项目'
)
async def create_project(
    project: ProjectInCreate
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
    project_category: BaseProjectCategory
):
    crud.create_project_category(project_category)
    return {
        'status': 'ok'
    }
