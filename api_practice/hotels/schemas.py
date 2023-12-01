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
    """{
      "rooms_quantity": 20,
      "name": "Cosmos Collection Altay Resort",
      "location": "Республика Алтай, Майминский район, село Урлу-Аспак, Лесхозная улица, 20",
      "image_id": 1,
      "services": [
        "Wi-Fi",
        "Parking"
      ],
      "id": 1
    }"""

    rooms_quantity: PositiveInt
    name: str
    location: str
    image_id: PositiveInt
    services: list[str]
    id: PositiveInt
