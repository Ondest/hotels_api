from datetime import date

from pydantic import BaseModel


class Bookings(BaseModel):
    room_id: int
    start_date: date
    end_date: date
    sea_window: bool = False
