from contextlib import asynccontextmanager

import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from src.Bookings.router import router as bookings_router
from src.hotels.rooms.router import router as rooms_router
from src.hotels.router import router as hotels_router
from src.images.router import router as images_router
from src.pages.router import router as pages_router
from src.Users.router import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_transaction=True
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi_cache")
    yield


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="src/static"), "static")

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
