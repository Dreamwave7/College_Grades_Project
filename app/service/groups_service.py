from sqlalchemy import select, insert, delete
from app.database.schemas import *
from app.database.models import *
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status


class GroupService:
    @staticmethod
    async def create_group(name: str, session: AsyncSession):
        query = insert(Groups).values(name=name).returning(Groups.id, Groups.name)
        adding = await session.execute(query)
        await session.commit()
        return adding.mappings().first()

    @staticmethod
    async def get_groups(session: AsyncSession):
        query = select(Groups)
        executing = await session.execute(query)
        result = [group[0] for group in executing.all()]
        return result

    @staticmethod
    async def remove_group(group_id: int, session: AsyncSession):
        query = delete(Groups).where(Groups.id == group_id)
        executing = await session.execute(query)
        await session.commit()
        return {"delete": "success"}
