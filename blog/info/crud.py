from blog.info.models import InfoModel, BlogrolModel
from blog.info.schemas import InfoOut, InfoIn, BlogrolList, Blogrol, BlogrolIn, AboutOut


def retrive_info():
    info_model: InfoModel = InfoModel.select().get()
    info = InfoOut.from_orm(info_model)
    return info


def create_info(info: InfoIn):
    InfoModel.create(**info.dict())


def list_blogrol():
    blogrols_model = BlogrolModel.select()
    blogrols = BlogrolList()
    for blogrol_model in blogrols_model:
        blogrols.blogrols.append(Blogrol.from_orm(blogrol_model))
    return blogrols


def create_blogrol(blogrol: BlogrolIn):
    BlogrolModel.create(**blogrol.dict())


def retrive_about():
    info_model: InfoModel.InfoModel.select().get()
    about = AboutOut.from_orm(info_model)
    return about