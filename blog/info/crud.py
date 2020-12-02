from typing import List, Optional

from blog.info.models import InfoModel, BlogrolModel
from blog.info.schemas import InfoOut, InfoIn, BlogrolIn, AboutOut, BlogrolOut


def retrive_info():
    info_model: InfoModel = InfoModel.select().get()
    info = InfoOut.from_orm(info_model)
    return info


def create_info(info: InfoIn):
    InfoModel.create(**info.dict())


def list_blogrol() -> Optional[List[BlogrolOut]]:
    blogrols_model = BlogrolModel.select()
    result = []
    for blogrol_model in blogrols_model:
        result.append(BlogrolOut.from_orm(blogrol_model))
    return result


def create_blogrol(blogrol: BlogrolIn):
    BlogrolModel.create(**blogrol.dict())


def retrive_about():
    info_model: InfoModel = InfoModel.select().get()
    about = AboutOut.from_orm(info_model)
    return about