from datetime import date

from api_practice.Bookings.models import Bookings
from api_practice.db import async_session_maker
from api_practice.hotels.rooms.models import Rooms
from dao.base import BaseDAO
from sqlalchemy import DATE, func, select

from sqlalchemy.sql.functions import coalesce


class RoomsDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def find_all(cls, hotel_id: int, date_from: date, date_to: date):
        rooms_query = select(func.count(1)).filter(
            Rooms.hotel_id == hotel_id,
            Bookings.rooms_id == Rooms.id,
            func.daterange(Bookings.date_from, Bookings.date_to, "[]").op("&&")(
                func.daterange(date_from, date_to, "[]"),
            ),
        )
        free_rooms_query = select(
            Rooms.id,
            Rooms.hotel_id,
            Rooms.name,
            Rooms.description,
            Rooms.services,
            Rooms.price,
            Rooms.quantity,
            (Rooms.price * func.date_part("day", date_to - date_from)).label(
                "total_price"
            ),
            (Rooms.quantity - rooms_query.subquery()).label("rooms_left"),
        ).filter(Rooms.hotel_id == hotel_id)

        async with async_session_maker() as session:
            result = await session.execute(free_rooms_query)
            return result.mappings().all()
