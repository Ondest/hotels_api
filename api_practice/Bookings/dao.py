from datetime import date

from api_practice.dao.base import BaseDAO
from api_practice.db import async_session_maker
from api_practice.hotels.rooms.models import Rooms
from sqlalchemy import func, insert, select

from .models import Bookings


class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(cls, user_id, rooms_id: int, date_from: date, date_to: date):
        """
        select
            quantity - (select count(1) from bookings
                     where rooms_id = 12 and (date_to, date_from) overlaps('2023-06-10', '2023-06-14')) as free
        from rooms
        where id = 12
        """
        free_rooms_query = (
            select(func.count(1))
            .filter(
                Bookings.rooms_id == Rooms.id,
                func.daterange(Bookings.date_from, Bookings.date_to, "[]").op("&&")(
                    func.daterange(date_from, date_to, "[]")
                ),
            )
            .as_scalar()
        )
        rooms_left = select((Rooms.quantity - free_rooms_query).label("free")).where(
            Rooms.id == rooms_id
        )

        async with async_session_maker() as session:
            free_rooms = await session.execute(rooms_left)
            if free_rooms.mappings().all()[0]["free"] > 0:
                get_price = select(Rooms.price).filter_by(id=rooms_id)
                price = await session.execute(get_price)
                add_booking = (
                    insert(Bookings)
                    .values(
                        rooms_id=rooms_id,
                        users_id=user_id,
                        date_from=date_from,
                        date_to=date_to,
                        price=price.scalar(),
                    )
                    .returning(Bookings)
                )
                new_booking = await session.execute(add_booking)
                await session.commit()
                return new_booking.scalar()
