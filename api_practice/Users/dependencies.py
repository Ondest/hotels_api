from datetime import datetime

from api_practice.exceptions import (
    NoCookieException,
    TokenExpiredException,
    TokenFormatException,
    UserIsntExistException,
)
from api_practice.Users.auth import ALGO, SECRET_KEY
from api_practice.Users.dao import UsersDAO
from fastapi import Depends, Request
from jose import jwt, JWTError


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise NoCookieException()
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGO)
    except JWTError:
        raise TokenFormatException()
    expire = payload.get("exp")
    if not expire or int(expire) < datetime.utcnow().timestamp():
        raise TokenExpiredException()
    user_id = payload.get("sub")
    if not user_id:
        raise UserIsntExistException()
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserIsntExistException()
    return user
