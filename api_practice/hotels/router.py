from datetime import date
from typing import Annotated

from api_practice.hotels.dao import HotelsDAO

from fastapi import APIRouter, Depends, Query


router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"],
)


async def common_parameters(
    date_from: date,
    date_to: date,
    location: Annotated[str, Query(max_length=30)],
):
    return {
        "location": location,
        "date_from": date_from,
        "date_to": date_to,
    }


@router.get("")
async def get_hotels(commons: Annotated[dict, Depends(common_parameters)]):
    hotels = await HotelsDAO.find_all(**commons)
    return hotels


@router.get("/{hotel_id}")
async def get_hotel(hotel_id: int):
    return await HotelsDAO.find_by_id(hotel_id)
