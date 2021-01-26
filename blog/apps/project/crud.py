from typing import List

from peewee import ModelSelect

from blog.apps.project.model import ProjectModel, ProjectCategoryModel
from blog.apps.project.schemas import ProjectInResponse, ProjectCategoryInProject, BaseProjectCategory, \
    ProjectCategoryInResponse, ProjectInProjectCategory, ProjectInUpdate


def create_project(project):
    ProjectModel.create(**project.dict())


def retrive_project_by_id(id: int) -> ProjectInResponse:
    project_model: ProjectModel = ProjectModel.get_by_id(id)
    project = ProjectInResponse.from_orm(project_model)
    project.category = ProjectCategoryInProject.from_orm(ProjectCategoryModel.get_by_id(project_model.category_id))
    return project


def update_project_by_id(id: int, project: ProjectInUpdate) -> ProjectInResponse:
    ProjectModel.update(**project.dict(exclude_unset=True)).where(ProjectModel.id == id).execute()
    return retrive_project_by_id(id)


def delete_project_by_id(id: int):
    ProjectModel.delete().where(ProjectModel.id == id).execute()


def create_project_category(category: BaseProjectCategory):
    ProjectCategoryModel.create(**category.dict())


def retrive_project_category_by_id(id: int):
    category_model: ProjectCategoryModel = ProjectCategoryModel.get_by_id(id)
    category = ProjectCategoryInResponse.from_orm(category_model)
    return category


def update_project_category_by_id(id: int, category: BaseProjectCategory):
    ProjectCategoryModel.update(**category.dict()).where(ProjectCategoryModel.id == id).execute()


def delete_project_category_by_id(id: int):
    ProjectCategoryModel.delete().where(ProjectCategoryModel.id == id).execute()


def list_project_category():
    categories_model: ModelSelect = ProjectCategoryModel.select()
    result = []
    for category_model in categories_model:
        category_model: ProjectCategoryModel
        category: ProjectCategoryInResponse = ProjectCategoryInResponse.from_orm(category_model)
        category.projects = []
        for project_id in category_model.projects_set:
            project_model = ProjectModel.get_by_id(project_id)
            project = ProjectInProjectCategory.from_orm(project_model)
            category.projects.append(project)
        result.append(category)
    return result


def retrive_projects() -> List[ProjectInResponse]:
    projects = ProjectModel.select(ProjectModel.id)
    result = []
    for project in projects:
        result.append(retrive_project_by_id(project.id))
    return result


def retrive_project_categories_simple() -> List[ProjectCategoryInProject]:
    project_categories = ProjectCategoryModel.select()
    result = []
    for category in project_categories:
        result.append(ProjectCategoryInProject.from_orm(category))
    return result
