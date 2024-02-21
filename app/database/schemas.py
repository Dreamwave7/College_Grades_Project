from pydantic import BaseModel, ConfigDict

class OrmBaseModel(BaseModel):
    class Config:
        from_attributes = True

class TeachersResponse(OrmBaseModel):
    id: int
    name: str