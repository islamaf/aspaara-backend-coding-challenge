from db.session import SessionLocal

from db.session import Base, engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
