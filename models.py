
from sqlalchemy import Column, Integer, String

from database import Base

class DefinitionModel (Base):
    __tablename__ = "definition"

    id = Column(Integer, primary_key=True, index=True, )
    simplified = Column(String, index=True)
    traditional = Column(String, index=True)
    pinyin = Column(String, index=True)
    english = Column(String, index=True)
