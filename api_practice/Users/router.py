from api_practice.exceptions import (
    InvalidEmailOrPasswordException,
    UserAlreadyExistsException,
)
from api_practice.Users.auth import (
    authenticate_user,
    create_access_token,
    get_password_hash,
)
from api_practice.Users.dao import UsersDAO
from api_practice.Users.schemas import SUserAuth
from fastapi import APIRouter, Response

router = APIRouter(
    prefix="/auth",
    tags=["Аутентификация и авторизация"],
)


@router.post("/register")
async def register_user(user_data: SUserAuth):
    user_exists = UsersDAO.find_one_or_none(email=user_data.email)
    if not user_exists:
        raise UserAlreadyExistsException()
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)
    return {"register": "success"}


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise InvalidEmailOrPasswordException()
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return {"login": "success"}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")
    return {"logout": "success"}
