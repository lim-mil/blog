from http import HTTPStatus
from typing import Any

from fastapi.responses import Response, JSONResponse


class ResponseContent:
    code: int
    message: str
    data: Any

    def __init__(self, *, code: int, message: str = '', data: Any = None):
        self.code = code
        self.message = message
        self.data = data

    def to_dict(self):
        return {
            'code': self.code,
            'message': self.message,
            'data': self.data
        }


def resp_200(*, data: Any = None, msg: str = 'OK') -> Response:
    return JSONResponse(
        status_code=HTTPStatus.OK,
        content=ResponseContent(code=HTTPStatus.OK, message=msg, data=data).to_dict()
    )


def resp_201(*, data: Any, msg: str = 'Created') -> Response:
    return JSONResponse(
        status_code=HTTPStatus.CREATED,
        content=ResponseContent(code=HTTPStatus.CREATED, message=msg, data=data).to_dict()
    )


def resp_400(*, data: Any = None, msg: str = 'Bad Request') -> Response:
    return JSONResponse(
        status_code=HTTPStatus.BAD_REQUEST,
        content=ResponseContent(code=HTTPStatus.BAD_REQUEST, message=msg).to_dict()
    )


def resp_401(*, data: Any = None, msg: str = 'Unauthorized') -> Response:
    return JSONResponse(
        status_code=HTTPStatus.UNAUTHORIZED,
        content=ResponseContent(code=HTTPStatus.UNAUTHORIZED, message=msg).to_dict()
    )


def resp_403(*, data: Any = None, msg: str = 'Forbidden') -> Response:
    return JSONResponse(
        status_code=HTTPStatus.FORBIDDEN,
        content=ResponseContent(code=HTTPStatus.FORBIDDEN, message=msg).to_dict()
    )


def resp_404(*, data: Any = None, msg: str = 'Not Found') -> Response:
    return JSONResponse(
        status_code=HTTPStatus.NOT_FOUND,
        content=ResponseContent(code=HTTPStatus.NOT_FOUND, message=msg).to_dict()
    )


def resp_405(*, data: Any = None, msg: str = 'Mmethod Not Allowed') -> Response:
    return JSONResponse(
        status_code=HTTPStatus.METHOD_NOT_ALLOWED,
        content=ResponseContent(code=HTTPStatus.METHOD_NOT_ALLOWED, message=msg).to_dict()
    )
