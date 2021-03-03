from blog.apps.oauth.models import OauthModel
from blog.apps.oauth.schemas import OauthInResponse


def retriveOauthById(id: int):
    global oauth_model
    try:
        oauth_model = OauthModel.get_by_id(id)
    except Exception as e:
        pass
    oauth = OauthInResponse.from_orm(oauth_model)
    return oauth


def retriveOauthByLogin(login: str):
    return OauthModel.get_or_none(OauthModel.login==login)


def createOauth(**kwargs) -> OauthModel:
    return OauthModel.create(**kwargs)
