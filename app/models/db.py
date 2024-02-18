from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.types import DateTime

DBURL = "postgresql+asyncpg://wmbufrxt:kznk4qJfbU8uiVGFubDWKfR0fAKxx6pX@trumpet.db.elephantsql.com/wmbufrxt"


class Base(DeclarativeBase):
    pass

class Students(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer(),primary_key=True)
    name: Mapped[str] = mapped_column(String(length=20), nullable=False)
    lastname: Mapped[str] = mapped_column(String(length=20), nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey("groupss.id"), nullable= False)

class Groups(Base):
    __tablename__ = "groupss"
    id:Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(length=5),nullable=False)

class Subjects(Base):
    __tablename__ = "subjects"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(length=20), nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"), nullable=False)

class Grades(Base):
    __tablename__ = "grades"
    id:Mapped[int] = mapped_column(Integer(),primary_key=True)
    grade: Mapped[int] = mapped_column(Integer(),nullable=False)
    student_id:Mapped[int] = mapped_column(ForeignKey("students.id"), nullable=False)
    subject_id:Mapped[int] = mapped_column(ForeignKey("subjects.id"),nullable= False)
    date:Mapped[DateTime] = mapped_column(DateTime)

class Teachers(Base):
    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(Integer(), primary_key= True)
    name:Mapped[str] = mapped_column(String(length=30))




