from typing import List
from fastapi import APIRouter, Form, Depends, Query
from app.database.schemas_Responses import *
from app.database.models import *
from app.database.db import get_session
from app.database.schemas import *
from sqlalchemy import select, insert
from app.service import teachers_service as ts
from app.service import groups_service as gs
from app.service.subject_service import SubjectService
from app.service.students_service import StudentsService

router = APIRouter(prefix="/edit")


@router.post("/teacher", tags=["Teachers"])
async def add_teacher(teacher: TeachersScheme, session=Depends(get_session)):
    add_to_db = await ts.add_teacher(teacher, session)
    return add_to_db


@router.get("/teachers", response_model=List[TeachersResponse], tags=["Teachers"])
async def get_teachers(session=Depends(get_session)):
    executing = await ts.get_teachers(session)
    return executing


@router.get("/teacher/{id_teacher}", response_model=TeachersResponse, tags=["Teachers"])
async def get_teacher(id_teacher: int, session=Depends(get_session)):
    result = await ts.get_teacher_by_id(id_teacher, session)
    return result


@router.post("/group", tags=["Groups"])
async def create_group(group: GroupScheme, session=Depends(get_session)):
    result = await gs.create_group(group.name, session)
    return result


@router.get("/groups", tags=["Groups"], response_model=List[GroupResponse])
async def get_groups(session=Depends(get_session)):
    result = await gs.get_groups(session)
    return result


@router.post("/student", tags=["Students"], response_model=StudentResponse)
async def create_student(student: StudentScheme, session=Depends(get_session)):
    adding = await StudentsService.create_student(student, session)
    return adding


@router.get("/students", tags=["Students"], response_model=list[StudentScheme])
async def get_students(session=Depends(get_session)):
    result = await StudentsService.get_all_students(session)
    return result

@router.post("/subjects", tags=["Subjects"], response_model=SubjectResponse)
async def create_subject(subject:SubjectScheme, session = Depends(get_session)):
    result = await SubjectService.create_subject(subject, session)
    return result

@router.get("/subjects",tags= ["Subjects"], response_model=List[SubjectResponse])
async def get_subjects(session = Depends(get_session)):
    result = await SubjectService.get_subjects(session)
    return result  

