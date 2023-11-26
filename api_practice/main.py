import uvicorn
from api_practice.Bookings.router import router as bookings_router
from api_practice.hotels.rooms.router import router as rooms_router
from api_practice.hotels.router import router as hotels_router
from api_practice.Users.router import router as user_router
from fastapi import FastAPI


app = FastAPI()

app.include_router(user_router)
app.include_router(bookings_router)
app.include_router(hotels_router)
app.include_router(rooms_router)


def main():
    uvicorn.run("main:app", reload=True)


if __name__ == "__main__":
    main()
