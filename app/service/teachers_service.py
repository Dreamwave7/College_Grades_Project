from sqlalchemy import select, insert, delete
from app.database.schemas import *
from app.database.models import *
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status


class TeacherService:
    @staticmethod
    async def add_teacher(teacher: TeachersScheme, session: AsyncSession):
        query = (
            insert(Teachers)
            .values(name=teacher.name)
            .returning(Teachers.id, Teachers.name)
        )
        adding = await session.execute(query)
        await session.commit()
        return adding.mappings().first()

    @staticmethod
    async def get_teachers(session: AsyncSession):
        query = select(Teachers)
        test = Teachers
        executing = await session.execute(query)
        result = executing.all()
        teachers_list = [teacher[0] for teacher in result]
        return teachers_list

    @staticmethod
    async def get_teacher_by_id(id_teacher: int, session: AsyncSession):
        query = select(Teachers).where(Teachers.id == id_teacher)
        executing = await session.execute(query)
        result = executing.first()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return result[0]

    @staticmethod
    async def remove_teacher(id_teacher: int, session: AsyncSession):
        query = delete(Teachers).where(Teachers.id == id_teacher)
        executing = await session.execute(query)
        await session.commit()
        return {"delete": "success"}
