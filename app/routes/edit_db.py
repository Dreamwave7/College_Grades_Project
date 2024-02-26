from fastapi import APIRouter, Form, Depends
from app.database.models import *
from app.database.db import get_session
from app.database.schemas import *
from sqlalchemy import select, insert

router = APIRouter(prefix="/edit", tags=["Teachers"])


@router.post("/add_teacher")
async def add_teacher(name: Form, session = Depends(get_session)):


    await session.commit()

    return "Done"




