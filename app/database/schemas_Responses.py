from app.database.schemas import OrmBaseModel



class TeachersResponse(OrmBaseModel):
    id: int
    name:str

class GroupResponse(OrmBaseModel):
    id: int
    name: str