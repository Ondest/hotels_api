from datetime import datetime, timedelta

from decouple import config
from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from src.users.dao import UsersDAO

SECRET_KEY = config("SECRET_KEY")
ALGO = config("ALGO")


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def vetify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGO)
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one_or_none(email=email)
    if not user:
        return None
    print(user.__dict__)
    if not vetify_password(password, user.hashed_password):
        return None
    return user
