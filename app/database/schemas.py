from pydantic import BaseModel, ConfigDict

class OrmBaseModel(BaseModel):
    class Config:
        from_attributes = True

class TeachersScheme(OrmBaseModel):
    name: str

class TestScheme(OrmBaseModel):
    test:str

class TeachersResponse(OrmBaseModel):
    id: int
    name:str