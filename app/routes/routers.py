from typing import List
from fastapi import APIRouter, Depends
from app.database.schemas_Responses import *
from app.database.models import *
from app.database.db import get_session
from app.database.schemas import *
from app.service.teachers_service import TeacherService
from app.service.groups_service import GroupService
from app.service.subject_service import SubjectService
from app.service.students_service import StudentsService
from app.service.grades_service import GradesService

router = APIRouter(prefix="/edit")


@router.post("/teacher", tags=["Teachers"], response_model=TeachersResponse)
async def add_teacher(teacher: TeachersScheme, session=Depends(get_session)):
    add_to_db = await TeacherService.add_teacher(teacher, session)
    return add_to_db


@router.get("/teachers", tags=["Teachers"], response_model=List[TeachersResponse])
async def get_teachers(session=Depends(get_session)):
    executing = await TeacherService.get_teachers(session)
    return executing


@router.get("/teacher/{id_teacher}", tags=["Teachers"], response_model=TeachersResponse)
async def get_teacher(id_teacher: int, session=Depends(get_session)):
    result = await TeacherService.get_teacher_by_id(id_teacher, session)
    return result


@router.delete("/teacher/{id_teacher}", tags=["Teachers"])
async def remove_teacher(id_teacher: int, session=Depends(get_session)):
    result = await TeacherService.remove_teacher(id_teacher, session)
    return result


@router.post("/group", tags=["Groups"], response_model=GroupResponse)
async def create_group(group: GroupScheme, session=Depends(get_session)):
    result = await GroupService.create_group(group.name, session)
    return result


@router.get("/groups", tags=["Groups"], response_model=List[GroupResponse])
async def get_groups(session=Depends(get_session)):
    result = await GroupService.get_groups(session)
    return result


@router.delete("/group/{group_id}", tags=["Groups"])
async def remove_group(group_id: int, session=Depends(get_session)):
    result = await GroupService.remove_group(group_id, session)
    return result


@router.post("/students", tags=["Students"], response_model=StudentResponse)
async def create_student(student: StudentScheme, session=Depends(get_session)):
    adding = await StudentsService.create_student(student, session)
    return adding


@router.get("/students", tags=["Students"], response_model=list[StudentResponse])
async def get_students(session=Depends(get_session)):
    result = await StudentsService.get_all_students(session)
    return result


@router.delete("/students/{id_student}", tags=["Students"])
async def remove_student(id_student: int, session=Depends(get_session)):
    result = await StudentsService.delete_student(id_student, session)
    return result


@router.post("/subjects", tags=["Subjects"], response_model=SubjectResponse)
async def create_subject(subject: SubjectScheme, session=Depends(get_session)):
    result = await SubjectService.create_subject(subject, session)
    return result


@router.get("/subjects", tags=["Subjects"], response_model=List[SubjectResponse])
async def get_subjects(session=Depends(get_session)):
    result = await SubjectService.get_subjects(session)
    return result


@router.delete("/subjects/{id_subject}", tags=["Subjects"])
async def remove_subject(id_subject: int, session=Depends(get_session)):
    result = await SubjectService.delete_subject(id_subject, session)
    return result


@router.post("/grades", tags=["Grades"], response_model=GradesScheme)
async def create_grade(grade: GradesScheme, session=Depends(get_session)):
    result = await GradesService.create_grade(grade, session)
    return result


@router.get("/grades", tags=["Grades"], response_model=List[GradesResponse])
async def get_grades(session=Depends(get_session)):
    result = await GradesService.get_all_grades(session)
    return result


@router.get("/test_query", tags=["Grades"], response_model=List[GradeQueryResponse])
async def get_students_grades(session=Depends(get_session)):
    result = await GradesService.get_grades_for_students(session)
    return result


@router.delete("/grade/{id_grade}", tags=["Grades"])
async def remove_grade(id_grade: int, session=Depends(get_session)):
    result = await GradesService.delete_grade(id_grade, session)
    return result
