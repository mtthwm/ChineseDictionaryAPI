from pydantic import BaseModel

from database import Base

class BaseDefinitionSchema (BaseModel):
    simplified: str
    traditional: str
    pinyin: str
    english: str

class DefinitionSchema (BaseDefinitionSchema):
    id: int

    class Config ():
        orm_mode = True

class CreateDefinitionSchema (BaseDefinitionSchema):
    pass