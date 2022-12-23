from typing import Type, TypeVar
from sqlalchemy.orm import Session
from db.session import Base

ModelType = TypeVar("ModelType", bound=Base)


class Repository():
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def all(self, db: Session):
        return db.query(self.model).all()

    async def add_get_record(self, db: Session, model, **obj):
        instance = db.query(model).filter_by(**obj).one_or_none()
        if instance:
            return instance

        record = model(**obj)
        db.add(record)
        db.flush()
        return record
