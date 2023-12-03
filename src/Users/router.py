from fastapi import APIRouter, Response
from src.exceptions import InvalidEmailOrPasswordException, UserAlreadyExistsException
from src.Users.auth import authenticate_user, create_access_token, get_password_hash
from src.Users.dao import UsersDAO
from src.Users.schemas import SUserAuth

router = APIRouter(
    prefix="/auth",
    tags=["Аутентификация и авторизация"],
)


@router.post("/register")
async def register_user(user_data: SUserAuth) -> None:
    user_exists = UsersDAO.find_one_or_none(email=user_data.email)
    if not user_exists:
        raise UserAlreadyExistsException()
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth) -> None:
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise InvalidEmailOrPasswordException()
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)


@router.post("/logout")
async def logout_user(response: Response) -> None:
    response.delete_cookie("booking_access_token")
