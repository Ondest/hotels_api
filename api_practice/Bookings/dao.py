from .models import Bookings
from api_practice.dao.base import BaseDAO


class BookingDAO(BaseDAO):
    model = Bookings
