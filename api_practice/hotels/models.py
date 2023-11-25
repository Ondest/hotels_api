from api_practice.db import Base
from sqlalchemy import Column, Integer, String, JSON


class Hotels(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)
    services = Column(JSON)
    rooms_quantity = Column(Integer)
    image_id = Column(Integer)
