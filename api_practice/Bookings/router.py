from datetime import date

from api_practice.Bookings.schemas import SBooking

from api_practice.exceptions import CantAddBookingException
from api_practice.Users.dependencies import get_current_user
from api_practice.Users.models import Users
from fastapi import APIRouter, Depends

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
):
    result = await BookingDAO.add(user.id, rooms_id, date_to, date_from)
    if not result:
        raise CantAddBookingException()
    return result
