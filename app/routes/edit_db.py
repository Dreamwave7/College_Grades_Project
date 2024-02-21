from fastapi import APIRouter, Form
from app.database.models import *
from app.database.db import get_session
from app.database.schemas import TeachersResponse
from sqlalchemy import select, insert

router = APIRouter(prefix="/edit")


@router.post("/add_teacher", response_model=TeachersResponse)
async def add_teacher(name: str):
    session = await get_session()
    # result = await session.execute(insert(Teachers).values(name = name))

    new_teacher = Teachers(name=name)
    session.add(new_teacher)
    await session.commit()
    return new_teacher






