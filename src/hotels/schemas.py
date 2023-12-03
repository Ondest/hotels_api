from pydantic import BaseModel, PositiveInt


class HotelInfo(BaseModel):
    id: PositiveInt
    name: str
    location: str
    services: list[str]
    rooms_quantity: PositiveInt
    image_id: PositiveInt
    rooms_left: int


class Hotel(BaseModel):
    rooms_quantity: PositiveInt
    name: str
    location: str
    image_id: PositiveInt
    services: list[str]
    id: PositiveInt
