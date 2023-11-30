import asyncio
from typing import Annotated

from api_practice.hotels.dao import HotelsDAO
from api_practice.hotels.dependencies import common_parameters

from api_practice.hotels.schemas import HotelInfo

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from pydantic import parse_obj_as


router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"],
)


@router.get("")
@cache(expire=30)
async def get_hotels(commons: Annotated[dict, Depends(common_parameters)]):
    await asyncio.sleep(4)
    hotels = await HotelsDAO.find_all(**commons)
    hotels_json = parse_obj_as(list[HotelInfo], hotels)
    return hotels_json


@router.get("/{hotel_id}")
async def get_hotel(hotel_id: int):
    return await HotelsDAO.find_by_id(hotel_id)
