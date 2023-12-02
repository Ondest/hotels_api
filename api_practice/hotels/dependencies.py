from datetime import date

from fastapi import Query


async def hotels_router_args(
    date_from: date,
    date_to: date,
    location: str = Query(None, max_length=30),
):
    return {
        "location": location,
        "date_from": date_from,
        "date_to": date_to,
    }
