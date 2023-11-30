from pydantic import BaseModel, Json, PositiveInt


class HotelInfo(BaseModel):
    """{
      "id": 1,
      "name": "Cosmos Collection Altay Resort",
      "location": "Республика Алтай, Майминский район, село Урлу-Аспак, Лесхозная улица, 20",
      "services": [
        "Wi-Fi",
        "Parking"
      ],
      "rooms_quantity": 20,
      "image_id": 1,
      "rooms_left": 20
    },"""

    id: PositiveInt
    name: str
    location: str
    services: Json
    rooms_quantity: PositiveInt
    image_id: PositiveInt
    rooms_left: int

    class Config:
        orm_mode = True
