from decouple import config
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DB_HOST = config("DB_HOST")  # "localhost"
DB_PORT = config("DB_PORT")  # "5999"
DB_USER = config("DB_USER")  # "postgres"
DB_PASS = config("DB_PASS")  # "postgres"
DB_NAME = config("DB_NAME")  # "postgres"

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    ...
