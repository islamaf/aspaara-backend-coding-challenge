from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from db.session import Base


class Talent(Base):
    __tablename__ = "talents"

    id = Column(String, primary_key=True)
    name = Column(String, index=True)
    grade = Column(String)

    plannings = relationship("Planning", backref="talent")
