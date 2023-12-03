from datetime import date

from fastapi import APIRouter, Depends

from src.bookings.schemas import SBooking

from src.exceptions import CantAddBookingException
from src.users.dependencies import get_current_user
from src.users.models import Users

from .dao import BookingDAO


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    result = await BookingDAO.find_all(users_id=user.id)
    return result


@router.post("")
async def add_booking(
    rooms_id: int,
    date_to: date,
    date_from: date,
    user: Users = Depends(get_current_user),
) -> SBooking | None:
    result = await BookingDAO.add(user.id, rooms_id, date_to, date_from)
    if not result:
        raise CantAddBookingException()
    return result


@router.delete("/{booking_id}")
async def delete_booking(
    booking_id: int, user: Users = Depends(get_current_user)
) -> None:
    await BookingDAO.delete_booking(bookings_id=booking_id, user_id=user.id)
