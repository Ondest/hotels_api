from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from src.hotels.dao import HotelsDAO
from src.hotels.dependencies import hotels_router_args
from src.hotels.schemas import Hotel, HotelInfo


router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"],
)


@router.get("")
@cache(expire=30)
async def get_hotels(
    commons: Annotated[dict, Depends(hotels_router_args)]
) -> list[HotelInfo]:
    hotels = await HotelsDAO.find_all(**commons)
    return hotels


@router.get("/{hotel_id}")
async def get_hotel(hotel_id: int) -> Hotel:
    return await HotelsDAO.find_by_id(hotel_id)
