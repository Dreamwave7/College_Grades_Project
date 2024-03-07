from sqlalchemy import delete, select, insert
from app.database.schemas import *
from app.database.models import *
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from random import randint


class StudentsService:
    @staticmethod
    async def create_student(student: StudentScheme, session: AsyncSession):
        query = (
            insert(Students)
            .values(
                name=student.name, lastname=student.lastname, group_id=student.group_id
            )
            .returning(Students.id, Students.name, Students.lastname, Students.group_id)
        )
        adding = await session.execute(query)
        await session.commit()
        return adding.mappings().first()

    @staticmethod
    async def get_all_students(session: AsyncSession):
        query = select(Students)
        executing = await session.execute(query)
        result = executing.fetchall()
        return [student[0] for student in result]

    @staticmethod
    async def delete_student(id_student: int, session: AsyncSession):
        query = delete(Students).where(Students.id == id_student)
        executing = await session.execute(query)
        await session.commit()
        return {"delete": "success"}
