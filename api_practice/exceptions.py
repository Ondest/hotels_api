from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"


class InvalidEmailOrPasswordException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Invalid email or password"


class TokenExpiredException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token expired"


class TokenFormatException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token is missing"


class UserIsntExistException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "User isn't exists"


class NoCookieException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detatil = "Incorrect cookie"
