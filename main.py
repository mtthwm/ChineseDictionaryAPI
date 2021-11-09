from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from typing import List
from sqlalchemy.orm.session import Session
from config import settings
import crud
from database import SessionLocal, engine
from schemas import CreateDefinitionSchema, DefinitionSchema
import models

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
async def root ():
    return {'message': 'Hello World'}

@app.get('/simplified_lookup/{word}', response_model=List[DefinitionSchema])
async def lookup_character (word: str, db: Session = Depends(get_db)):
    matches = crud.lookup_character(db, word)
    return matches


@app.get('/import_definitions')
async def import_definitions (db: Session = Depends(get_db)):
    if settings.allow_import:
        models.Base.metadata.drop_all(bind=engine)
        models.Base.metadata.create_all(bind=engine)
        from dictionary_parser import parsed_dict
        for one_dict in parsed_dict:
            try:
                crud.create_definition(db, CreateDefinitionSchema(
                    traditional = one_dict["traditional"], 
                    simplified = one_dict["simplified"], 
                    english = one_dict["english"], 
                    pinyin = one_dict["pinyin"])
                    )
            except Exception as e:
                print(one_dict)
                raise e
        return 200
    else:
        return HTTPException(403)