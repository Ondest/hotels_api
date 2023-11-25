from datetime import date
from typing import Annotated

import uvicorn
from api_practice.Bookings.router import router as bookings_router
from api_practice.Users.router import router as user_router
from fastapi import FastAPI, Query
from models import Bookings


app = FastAPI()

app.include_router(user_router)
app.include_router(bookings_router)


@app.get("/hotels/{hotel_id}")
async def get_hotels(
    hotel_id: int,
    start_date: date,
    end_date: date,
    rating: Annotated[int | None, Query(ge=1, le=5)] = None,
    wi_fi: Annotated[bool | None, Query()] = None,
):
    return hotel_id, start_date, end_date, wi_fi, rating


@app.post("/bookings")
async def add_bookings(bookings: Bookings):
    return f"{(bookings.end_date - bookings.start_date).days} days reserve"


def main():
    uvicorn.run("main:app", reload=True)


if __name__ == "__main__":
    main()
