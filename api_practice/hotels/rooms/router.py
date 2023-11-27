from datetime import date

from api_practice.hotels.rooms.dao import RoomsDAO
from fastapi import APIRouter, Query


router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("/{hotel_id}/rooms")
async def get_rooms(
    hotel_id: int, date_from: date, date_to: date, age: int = Query(ge=18, default=None)
):
    return await RoomsDAO.find_all(
        hotel_id=hotel_id, date_from=date_from, date_to=date_to
    )
