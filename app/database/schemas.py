from pydantic import BaseModel, ConfigDict

class OrmBaseModel(BaseModel):
    class Config:
        from_attributes = True

class TeachersScheme(OrmBaseModel):
    name: str

class GroupScheme(OrmBaseModel):
    name: str

class StudentScheme(OrmBaseModel):
    name:str
    lastname:str
    group_id:int

class SubjectScheme(OrmBaseModel):
    name:str
    teacher_id:int


class GradesScheme(OrmBaseModel):
    grade: int
    student_id:int
    subject_id:int
