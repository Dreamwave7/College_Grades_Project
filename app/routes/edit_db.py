from fastapi import APIRouter, Form, Depends
from app.database.models import *
from app.database.db import get_session
from app.database.schemas import *
from sqlalchemy import select, insert
from app.service import teachers_service as ts

router = APIRouter(prefix="/edit", tags=["Teachers"])


@router.post("/add_teacher")
async def add_teacher(teacher : TeachersScheme, session = Depends(get_session)):
    add_to_db = await ts.add_teacher(teacher, session)
    return add_to_db

@router.get("/teachers", response_model=TeachersResponse)
async def get_teachers(session = Depends(get_session)):
    executing = await ts.get_teachers(session)
    return executing




