from src.dao.base import BaseDAO
from src.Users.models import Users


class UsersDAO(BaseDAO):
    model = Users
