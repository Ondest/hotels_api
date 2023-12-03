from datetime import date

from fastapi import APIRouter

from src.hotels.rooms.dao import RoomsDAO


router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("/{hotel_id}/rooms")
async def get_rooms(hotel_id: int, date_from: date, date_to: date):
    return await RoomsDAO.find_all(
        hotel_id=hotel_id, date_from=date_from, date_to=date_to
    )
