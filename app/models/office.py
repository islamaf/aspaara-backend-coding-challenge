from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from db.session import Base


class Office(Base):
    __tablename__ = "offices"

    id = Column(Integer, primary_key=True)
    city = Column(String)
    postal_code = Column(String, nullable=False)

    plannings = relationship("Planning", backref="office")
