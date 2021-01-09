class BlogException(Exception):

    def __init__(self, msg: str = ''):
        super().__init__()
        self.msg = msg


class BAD_REQUEST_400_Exception(BlogException):
    pass


class UNAUTHORIZED_401_Exception(BlogException):
    pass


class FORBIDDEN_403_Exception(BlogException):
    pass


class NOT_FOUND_404_Exception(BlogException):
    pass


class METHOD_NOT_ALLOWED_405_Exception(BlogException):
    pass
