from datetime import date
from pydantic import BaseModel


class SBooking(BaseModel):
    id: int
    rooms_id: int
    users_id: int
    date_from: date
    date_to: date
    price: int

    class Config:
        orm_mode = True
