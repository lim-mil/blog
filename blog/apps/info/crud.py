from typing import List, Optional

from blog.apps.info.models import InfoModel, BlogrolModel
from blog.apps.info.schemas import BaseInfo, InfoInCreate, AboutInResponse, BaseBlogrol


def retrive_info():
    info_model: InfoModel = InfoModel.select().get()
    info = BaseInfo.from_orm(info_model)
    return info


def create_info(info: InfoInCreate):
    InfoModel.create(**info.dict())


def list_blogrol() -> List[BaseBlogrol]:
    blogrols_model = BlogrolModel.select()
    result = []
    for blogrol_model in blogrols_model:
        result.append(BaseBlogrol.from_orm(blogrol_model))
    return result


def create_blogrol(blogrol: BaseBlogrol):
    BlogrolModel.create(**blogrol.dict())


def retrive_about():
    info_model: InfoModel = InfoModel.select().get()
    about = AboutInResponse.from_orm(info_model)
    return about