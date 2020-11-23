from project.model import ProjectModel, ProjectCategoryModel
from project.schemas import ProjectOut, ProjectCategory, ProjectCategoryOut, ProjectUpdate, ProjectCategoryIn


def create_project(project):
    ProjectModel.create(**project.dict())


def retrive_project_by_id(id: int):
    project_model: ProjectModel = ProjectModel.get_by_id(id)
    project = ProjectOut.from_orm(project_model)
    project.category = ProjectCategoryOut.from_orm(ProjectCategoryModel.get_by_id(project_model.category_id))
    return project


def update_project_by_id(id: int, project: ProjectUpdate):
    ProjectModel.update(**project.dict(exclude_unset=True)).where(ProjectModel.id == id).execute()


def delete_project_by_id(id: int):
    ProjectModel.delete().where(ProjectModel.id == id).execute()


def create_project_category(category: ProjectCategoryIn):
    ProjectCategoryModel.create(**category.dict())


def retrive_project_category_by_id(id: int):
    category_model: ProjectCategoryModel = ProjectCategoryModel.get_by_id(id)
    category = ProjectCategoryOut.from_orm(category_model)
    return category


def update_project_category_by_id(id: int, category: ProjectCategoryIn):
    ProjectCategoryModel.update(**category.dict()).where(ProjectCategoryModel.id == id).execute()


def delete_project_category_by_id(id: int):
    ProjectCategoryModel.delete().where(ProjectCategoryModel.id == id).execute()
