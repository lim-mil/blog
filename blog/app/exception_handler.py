from fastapi import Request, FastAPI
from fastapi.exceptions import RequestValidationError

from blog.pkg.exception import BAD_REQUEST_400_Exception, FORBIDDEN_403_Exception
from blog.pkg.response import resp_400, resp_403


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(FORBIDDEN_403_Exception)
    async def forbidden_exception_handler(request: Request, exc: RequestValidationError):
        return resp_403()
