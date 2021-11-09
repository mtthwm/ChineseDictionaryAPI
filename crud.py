from schemas import DefinitionSchema
from models import DefinitionModel
from sqlalchemy.orm import Session
from sqlalchemy import or_
from sqlalchemy.sql.expression import func

def create_definition (db: Session, definition: DefinitionSchema):
    new_definition = DefinitionModel(simplified=definition.simplified, traditional=definition.traditional, pinyin=definition.pinyin, english=definition.english)
    db.add(new_definition)
    db.commit()
    db.refresh(new_definition)
    return new_definition

def lookup_character (db: Session, character: str):
        response = db.query(DefinitionModel).filter(
            or_(
                DefinitionModel.simplified.contains(character), 
                DefinitionModel.traditional.contains(character)
            )
        ).order_by(func.length(DefinitionModel.simplified)).all()
        return response
