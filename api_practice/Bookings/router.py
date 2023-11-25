from api_practice.Bookings.schemas import SBooking
from api_practice.Users.dependencies import get_current_user
from api_practice.Users.models import Users
from .dao import BookingDAO
from fastapi import APIRouter, Depends


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    print(user.id, user.email, user.hashed_password)
    result = await BookingDAO.find_all(user_id=user_id)
    return result
