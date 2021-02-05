from typing import List

from fastapi import APIRouter, Path, Depends

from blog.apps.project import crud
from blog.apps.project.schemas import ProjectCategoriesForResponse, ProjectInCreate, BaseProjectCategory, \
    ProjectInUpdate, ProjectForResponse, ProjectsForResponse, ProjectCategoriesSimpleForResponse, \
    ProjectCategoryForResponse
from blog.apps.user.models import UserModel
from blog.pkg.response import resp_200
from blog.pkg.security import get_current_user

router = APIRouter()


@router.get(
    '',
    description='',
    summary='获取所有项目',
    response_model=ProjectsForResponse
)
async def retrive_projects():
    data = crud.retrive_projects()
    return ProjectsForResponse(data=data)


@router.get(
    '/categories',
    description='',
    summary='获取所有项目分类',
    response_model=ProjectCategoriesForResponse
)
async def list_project_category():
    data = crud.list_project_category()
    return ProjectCategoriesForResponse(data=data)


@router.post(
    '',
    description='',
    summary='创建项目'
)
async def create_project(
    project: ProjectInCreate,
    user: UserModel = Depends(get_current_user)
):
    crud.create_project(project)
    return resp_200()


@router.post(
    '/categories',
    description='',
    summary='创建分类'
)
async def create_category(
    project_category: BaseProjectCategory,
    user: UserModel = Depends(get_current_user)
):
    crud.create_project_category(project_category)
    return resp_200()


@router.get(
    '/categories/simple',
    description='',
    summary='获取简单的项目分类信息',
    response_model=ProjectCategoriesSimpleForResponse
)
async def retrive_project_categories_simple():
    data = crud.retrive_project_categories_simple()
    return ProjectCategoriesSimpleForResponse(data=data)


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
    summary='更新项目',
    response_model=ProjectForResponse
)
async def update_project(
    project: ProjectInUpdate,
    project_id: int = Path(..., gt=0),
    user: UserModel = Depends(get_current_user)
):
    data = crud.update_project_by_id(project_id, project)
    return ProjectForResponse(data=data)


@router.get(
    '/{project_id}',
    description='',
    summary='获取项目',
    response_model=ProjectForResponse
)
async def retrive_project(
    project_id: int = Path(..., gt=0),
):
    project = crud.retrive_project_by_id(project_id)
    return ProjectForResponse(data=project)


@router.delete(
    '/categories/{project_category_id}',
    description='',
    summary='删除项目分类'
)
async def delete_project_category(
    project_category_id: int = Path(..., gt=0),
    user: UserModel = Depends(get_current_user)
):
    crud.delete_project_category_by_id(project_category_id)
    return resp_200()


@router.patch(
    '/categories/{project_category_id}',
    description='',
    summary='更新项目分类',
    response_model=ProjectCategoryForResponse
)
async def update_project_category(
    project_category: BaseProjectCategory,
    project_category_id: int = Path(..., gt=0),
    user: UserModel = Depends(get_current_user)
):
    data = crud.update_project_category_by_id(project_category_id, project_category)
    return ProjectCategoryForResponse(data=data)
