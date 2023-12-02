from typing import Annotated

from api_practice.hotels.dao import HotelsDAO
from api_practice.hotels.dependencies import hotels_router_args

from api_practice.hotels.schemas import Hotel, HotelInfo

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache


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
