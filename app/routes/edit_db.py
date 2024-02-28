from typing import List
from fastapi import APIRouter, Form, Depends, Query
from app.database.schemas_Responses import *
from app.database.models import *
from app.database.db import get_session
from app.database.schemas import *
from sqlalchemy import select, insert
from app.service import teachers_service as ts
from app.service import groups_services as gs

router = APIRouter(prefix="/edit")


@router.post("/teacher",tags=["Teachers"])
async def add_teacher(teacher : TeachersScheme, session = Depends(get_session)):
    add_to_db = await ts.add_teacher(teacher, session)
    return add_to_db

@router.get("/teachers", response_model=List[TeachersResponse],tags=["Teachers"])
async def get_teachers(session = Depends(get_session)):
    executing = await ts.get_teachers(session)
    return executing

@router.get("/teacher/{id_teacher}", response_model=TeachersResponse,tags=["Teachers"])
async def get_teacher(id_teacher:int, session = Depends(get_session)):
    result = await ts.get_teacher_by_id(id_teacher, session)
    return result




@router.post("/group", tags=["Groups"])
async def create_group(group:GroupScheme, session = Depends(get_session)):
    result = await gs.create_group(group.name, session)
    return result


@router.get("/groups", tags=["Groups"], response_model=List[GroupResponse])
async def get_groups(session = Depends(get_session)):
    result = await gs.get_groups(session)
    return result

    



