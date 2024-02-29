from sqlalchemy import select, insert
from app.database.schemas import *
from app.database.models import *
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status


async def create_group(name: str, session:AsyncSession):
    query = insert(Groups).values(name = name).returning(Groups.id,Groups.name)
    adding = await session.execute(query)
    await session.commit()
    return adding.mappings().first()



async def get_groups(session:AsyncSession):
    query = select(Groups)
    executing = await session.execute(query)
    result = [group[0] for group in executing.all()]
    return result

