from app.database.schemas import OrmBaseModel



class TeachersResponse(OrmBaseModel):
    id: int
    name:str

class GroupResponse(OrmBaseModel):
    id: int
    name: str

class StudentResponse(OrmBaseModel):
    id:int
    name:str
    lastname:str
    group_id:int













