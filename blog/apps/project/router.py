from typing import List

from fastapi import APIRouter, Path, Depends

from blog.apps.project import crud
from blog.apps.project.schemas import ProjectCategoriesForResponse, ProjectInCreate, BaseProjectCategory, \
    ProjectInUpdate, ProjectForResponse
from blog.apps.user.models import UserModel
from blog.pkg.response import resp_200
from blog.pkg.security import get_current_user

router = APIRouter()


@router.get(
    '/categories',
    description='',
    summary='获取所有项目分类',
    response_model=ProjectCategoriesForResponse
)
async def list_project_category():
    results = crud.list_project_category()
    return ProjectCategoriesForResponse(data=results)


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


@router.delete(
    '/{project_id}',
    description='',
    summary='删除项目',
)
async def delete_project(
    project_id:int = Path(..., gt=0),
    user: UserModel = Depends(get_current_user)
):
    crud.delete_project_by_id(project_id)
    return resp_200()


@router.patch(
    '/{project_id}',
    description='',
    summary='更新项目'
)
async def update_project(
    project: ProjectInUpdate,
    project_id: int = Path(..., gt=0),
    user: UserModel = Depends(get_current_user)
):
    crud.update_project_by_id(project_id, project)
    return resp_200()


@router.get(
    '/{project_id}',
    description='',
    summary='获取项目',
    response_model=ProjectForResponse
)
async def retrive_project(
    project_id: int = Path(..., gt=0),
    user: UserModel = Depends(get_current_user)
):
    project = crud.retrive_project_by_id(project_id)
    return ProjectForResponse(data=project)


@router.delete(
    '/{project_category_id}',
    description='',
    summary='删除项目分类'
)
async def delete_project_category(
    project_category_id: int = Path(..., gt=0),
    user: UserModel = Depends(get_current_user)
):
    crud.delete_project_category_by_id(project_category_id)
    return resp_200()

