import uvicorn
from api_practice.Bookings.router import router as bookings_router
from api_practice.hotels.rooms.router import router as rooms_router
from api_practice.hotels.router import router as hotels_router
from api_practice.images.router import router as images_router
from api_practice.pages.router import router as pages_router
from api_practice.Users.router import router as user_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="api_practice/static"), "static")

app.include_router(user_router)
app.include_router(bookings_router)
app.include_router(hotels_router)
app.include_router(pages_router)
app.include_router(rooms_router)
app.include_router(images_router)

origins = ["http:localhost"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Authorization",
    ],
)


def main():
    uvicorn.run("main:app", reload=True)


if __name__ == "__main__":
    main()
