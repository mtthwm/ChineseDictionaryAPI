from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from config import settings
from crud import create_definition
from database import SessionLocal, engine
from schemas import CreateDefinitionSchema
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

@app.get('/import_definitions')
async def import_definitions (db: Session = Depends(get_db)):
    models.Base.metadata.drop_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)
    from dictionary_parser import parsed_dict
    for one_dict in parsed_dict:
        try:
            print(one_dict['english'])
            create_definition(db, CreateDefinitionSchema(
                traditional = one_dict["traditional"], 
                simplified = one_dict["simplified"], 
                english = one_dict["english"], 
                pinyin = one_dict["pinyin"])
                )
        except Exception as e:
            print(one_dict)
            raise e
    return 200