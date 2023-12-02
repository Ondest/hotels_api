from datetime import date

from api_practice.Bookings.models import Bookings

from api_practice.db import async_session_maker
from api_practice.hotels.models import Hotels
from api_practice.hotels.rooms.models import Rooms
from dao.base import BaseDAO
from sqlalchemy import func, select

from sqlalchemy.sql.functions import coalesce


class HotelsDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def find_all(cls, location: str, date_from=date, date_to=date):
        async with async_session_maker() as session:
            query = select(
                Hotels.id,
                Hotels.name,
                Hotels.location,
                Hotels.services,
                Hotels.rooms_quantity,
                Hotels.image_id,
                coalesce(
                    Hotels.rooms_quantity
                    - select(1).filter(
                        Rooms.hotel_id == Hotels.id,
                        Bookings.rooms_id == Rooms.id,
                        func.daterange(Bookings.date_from, Bookings.date_to, "[]").op(
                            "&&"
                        )(
                            func.daterange(date_from, date_to, "[]"),
                        ),
                    ),
                    Hotels.rooms_quantity,
                ).label("rooms_left"),
            ).filter(Hotels.location.ilike(f"%{location.lower()}%"))

            result = await session.execute(query)
            return result.mappings().all()
