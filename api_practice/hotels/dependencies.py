from datetime import date

from fastapi import Query


async def common_parameters(
    date_from: date,
    date_to: date,
    location: str = Query(None, max_length=30),
):
    return {
        "location": location,
        "date_from": date_from,
        "date_to": date_to,
    }
