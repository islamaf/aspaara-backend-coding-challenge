from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from db.session import Base


class JobManager(Base):
    __tablename__ = "job_managers"

    id = Column(String, primary_key=True)
    name = Column(String)

    plannings = relationship("Planning", backref="job_manager")
