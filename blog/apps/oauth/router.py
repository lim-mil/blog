import json

import httpx
from fastapi import APIRouter
from httpx import AsyncClient

from blog.apps.oauth import crud
from blog.apps.oauth.schemas import OauthForResponse, OauthInResponse
from blog.pkg.response import resp_200
from blog.pkg.security import create_oauth_jwt_token

router = APIRouter()


@router.get(
    '/github',
    description='',
    summary='',
    # response_model=OauthForResponse
)
async def github_oauth(
    code: str,
    state: str
):
    data = {
        'client_id': '08534284cc7baa6ce7d4',
        'client_secret': '472d154c75d72f911403a6bcfbb520d10a542f5b',
        'code': code,
        'state': state
    }
    async with httpx.AsyncClient() as client:
        client: AsyncClient
        headers = {'Accept': 'application/json'}
        result = await client.post(url='https://github.com/login/oauth/access_token', data=data, headers=headers)
        result = json.loads(result.text)
        headers = {'Authorization': f'Bearer {result.get("access_token")}'}
        result = await client.get('https://api.github.com/user', headers=headers)
        result = json.loads(result.text)
        oauth_model = crud.retriveOauthByLogin(result.get('login'))
        if not oauth_model:
            oauth_model = crud.createOauth(**result)
        oauth = OauthInResponse.from_orm(oauth_model)
        token = create_oauth_jwt_token(oauth)
    return resp_200(data={
        'token': token,
        'oauth': oauth.dict()
    })