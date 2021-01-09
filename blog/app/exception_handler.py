from fastapi import Request, FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import *
from starlette.exceptions import HTTPException as StarletteHTTPException

from blog.pkg.exception import BAD_REQUEST_400_Exception, FORBIDDEN_403_Exception, UNAUTHORIZED_401_Exception
from blog.pkg.response import resp_400, resp_403, resp_401


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(FORBIDDEN_403_Exception)
    async def forbidden_exception_handler(request: Request, exc: FORBIDDEN_403_Exception):
        return resp_403()

    @app.exception_handler(UNAUTHORIZED_401_Exception)
    async def unauthorized_exception_handler(request: Request, exc: UNAUTHORIZED_401_Exception):
        return resp_401()

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        """
        重写默认异常处理器
        """
        return JSONResponse(
            status_code=exc.status_code,
            content={
                'code': exc.status_code,
                'message': exc.detail,
                'data': None
            }
        )