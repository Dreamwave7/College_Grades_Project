from fastapi import APIRouter
from app.models import db
from sqlalchemy import select, insert

router = APIRouter("/edit", tags=["Edit"])

@router.post("/add_teacher")
async def add_teacher(name:str):
    session = await db.get_session()
    session.execute(insert(db.Teachers).values(name = name))
    return "Donek"
