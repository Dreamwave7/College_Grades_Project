from pydantic import BaseModel, ConfigDict

class OrmBaseModel(BaseModel):
    class Config:
        from_attributes = True

class TeachersScheme(OrmBaseModel):
    name: str

class GroupScheme(OrmBaseModel):
    name: str

