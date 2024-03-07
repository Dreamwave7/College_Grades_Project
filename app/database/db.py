from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


DBURL = "postgresql+asyncpg://wmbufrxt:kznk4qJfbU8uiVGFubDWKfR0fAKxx6pX@trumpet.db.elephantsql.com/wmbufrxt"

engine = create_async_engine(DBURL)

Session = async_sessionmaker(engine)


async def get_session():
    async with Session() as connect:
        yield connect


class Base(DeclarativeBase):
    pass
