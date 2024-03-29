from .db import Base
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.types import DateTime


class Students(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(length=20), nullable=False)
    lastname: Mapped[str] = mapped_column(String(length=20), nullable=False)
    group_id: Mapped[int] = mapped_column(
        ForeignKey("groupss.id", ondelete="CASCADE"), nullable=False
    )


class Teachers(Base):
    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(length=30))


class Groups(Base):
    __tablename__ = "groupss"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(length=5), nullable=False)


class Subjects(Base):
    __tablename__ = "subjects"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(length=20), nullable=False)
    teacher_id: Mapped[int] = mapped_column(
        ForeignKey("teachers.id", ondelete="CASCADE"), nullable=False
    )


class Grades(Base):
    __tablename__ = "grades"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    grade: Mapped[int] = mapped_column(Integer(), nullable=False)
    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="CASCADE"), nullable=False
    )
    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False
    )
    date: Mapped[DateTime] = mapped_column(DateTime())
