from sqlalchemy import select, insert, and_
from app.database.schemas import *
from app.database.models import *
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
import datetime
from random import randint
import pprint


class GradesService:
    @staticmethod
    async def create_grade(grade: GradesScheme, session: AsyncSession):
        # query = insert(Grades).values(**grade.model_dump(), date = datetime.datetime.now().date()).returning(Grades.grade, Grades.student_id,Grades.subject_id)
        query = (
            insert(Grades)
            .values(
                grade=randint(1, 12),
                student_id=randint(9, 119),
                subject_id=randint(11, 20),
                date=datetime.datetime.now().date(),
            )
            .returning(Grades.grade, Grades.student_id, Grades.subject_id)
        )
        adding = await session.execute(query)
        await session.commit()
        return adding.mappings().first()

    @staticmethod
    async def get_all_grades(session: AsyncSession):
        query = select(Grades)
        executing = await session.execute(query)
        result = [grade[0] for grade in executing.fetchall()]
        return result

    @staticmethod
    async def get_grades_for_students(session: AsyncSession):
        query = (
            select(
                Grades.grade.label("Grade"),
                Students.name.label("Student_name"),
                Groups.name.label("Group"),
                Teachers.name.label("Teacher")).where(Grades.grade == 6)
            .select_from(Grades)
            .join(Students, Students.id == Grades.student_id)
            .join(Groups)
            .join(Subjects)
            .join(Teachers)
        )
        executing = await session.execute(query)
        return(executing)
