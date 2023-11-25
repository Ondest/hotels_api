from api_practice.db import Base
from sqlalchemy import Column, Integer, ForeignKey, Date


class Bookings(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, nullable=False)
    rooms_id = Column(ForeignKey("rooms.id"), nullable=False)
    users_id = Column(ForeignKey("users.id"), nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
