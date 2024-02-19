from fastapi import APIRouter
from app.models import db
from sqlalchemy import select, insert

router = APIRouter(prefix="/edit")

@router.post("/add_teacher")
async def add_teacher(name:str):
    session = await db.get_session()
    await session.execute(insert(db.Teachers).values(name = name))
    await session.commit()
    return "Donek"
