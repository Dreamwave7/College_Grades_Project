from sqlalchemy import select, insert
from app.database.schemas import *
from app.database.models import *
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
import datetime


class GradesService:
    @staticmethod
    async def create_grade(grade:GradesScheme, session:AsyncSession):
        query = insert(Grades).values(**grade.model_dump(), date = datetime.datetime.now().date())
        adding = await session.execute(query)
        await session.commit()
        return adding
        