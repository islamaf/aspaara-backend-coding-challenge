from sqlalchemy import Column, String, Integer, Float, DateTime, Boolean, JSON, ForeignKey

from db.session import Base


class Planning(Base):
    __tablename__ = "plannings"

    id = Column(Integer, primary_key=True)
    original_id = Column(String, nullable=False, unique=False)
    operating_unit = Column(String, nullable=False)
    total_hours = Column(Float, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    booking_grade = Column(String)
    industry = Column(String)
    required_skills = Column(JSON)
    optional_skills = Column(JSON)
    is_unassigned = Column(Boolean, nullable=False, default=True)

    client_id = Column(String, ForeignKey("clients.id"))
    office_id = Column(Integer, ForeignKey("offices.id"))
    talent_id = Column(String, ForeignKey("talents.id"))
    job_manager_id = Column(String, ForeignKey("job_managers.id"))
