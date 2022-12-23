from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from db.session import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(String, primary_key=True)
    name = Column(String)

    plannings = relationship("Planning", backref="client")
