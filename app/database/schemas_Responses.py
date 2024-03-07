from app.database.schemas import OrmBaseModel


class TeachersResponse(OrmBaseModel):
    id: int
    name: str


class GroupResponse(OrmBaseModel):
    id: int
    name: str


class StudentResponse(OrmBaseModel):
    id: int
    name: str
    lastname: str
    group_id: int


class SubjectResponse(OrmBaseModel):
    id: int
    name: str
    teacher_id: int


class GradeQueryResponse(OrmBaseModel):
    Grade: int
    Student_name: str
    Group: str
    Teacher: str


class GradesResponse(OrmBaseModel):
    id: int
    grade: int
    student_id: int
    subject_id: int
