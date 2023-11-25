from api_practice.dao.base import BaseDAO
from api_practice.Users.models import Users


class UsersDAO(BaseDAO):
    model = Users
