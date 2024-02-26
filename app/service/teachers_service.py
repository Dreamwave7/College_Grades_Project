from sqlalchemy import select, insert
from app.database.schemas import *
from app.database.models import *
from sqlalchemy.ext.asyncio import AsyncSession


async def add_teacher(teacher: TeachersScheme, session: AsyncSession):
    query = (
        insert(Teachers).values(name=teacher.name).returning(Teachers.id, Teachers.name)
    )
    adding = await session.execute(query)
    await session.commit()
    return adding.mappings().all()


async def get_teachers(session: AsyncSession):
    query = select(Teachers)
    executing = await session.execute(query)
    result = executing.first()
    return result[0]
