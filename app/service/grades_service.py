from sqlalchemy import select, insert
from app.database.schemas import *
from app.database.models import *
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
import datetime
from random import randint


class GradesService:
    @staticmethod
    async def create_grade(grade:GradesScheme, session:AsyncSession):
        # query = insert(Grades).values(**grade.model_dump(), date = datetime.datetime.now().date()).returning(Grades.grade, Grades.student_id,Grades.subject_id)
        query = insert(Grades).values(grade = randint(1,12),student_id = randint(9,119),subject_id =randint(11,20) , date = datetime.datetime.now().date()).returning(Grades.grade, Grades.student_id,Grades.subject_id)
        adding = await session.execute(query)
        await session.commit()
        return adding.mappings().first()

    @staticmethod
    async def get_all_grades(session:AsyncSession):
        query = select(Grades)
        executing = await session.execute(query)
        result = [grade[0] for grade in executing.fetchall()]
        return result
        
    @staticmethod
    async def get_grades_for_students(session:AsyncSession):
        # query = select(Grades.grade).label("grade").join(Subjects).join(Students).join(Teachers).join(Groups).where(Grades.student_id == 52)
        query = select(Grades.grade.label("grade"), Subjects.name.label("subject_name"), Students.name, Groups.name.label("group_name"), Teachers.name).join(Subjects).join(Teachers).join(Students).join(Groups)
        executing = await session.execute(query)

        for i in executing.fetchall():
            print(i._mapping)
        # print(executing.mappings().all())