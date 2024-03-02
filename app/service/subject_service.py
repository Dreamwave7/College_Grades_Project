from sqlalchemy import select, insert
from app.database.schemas import *
from app.database.models import *
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

class SubjectService: 
    @staticmethod
    async def create_subject(subject:SubjectScheme, session:AsyncSession):
        query = insert(Subjects).values(name = subject.name, teacher_id = subject.teacher_id ).returning(Subjects.id,Subjects.name, Subjects.teacher_id)
        adding = await session.execute(query)
        await session.commit()
        return adding.mappings().first()
    
    @staticmethod
    async def get_subjects(session:AsyncSession):
        query = select(Subjects)
        executing = await session.execute(query)
        result = [subject[0] for subject in executing.all()]
        return result
