import datetime
from pydantic import BaseModel
from typing import Optional, List

from schemas.skill import SkillSchema


def to_camel_case(snake_str: str) -> str:
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


class PlanningSchema(BaseModel):
    id: int
    original_id: str
    client_id: str
    operating_unit: str
    total_hours: float
    is_unassigned: bool
    start_date: datetime.datetime
    end_date: datetime.datetime
    required_skills: List[SkillSchema]
    optional_skills: List[SkillSchema]

    job_manager_id: Optional[str]
    job_manager_name: Optional[str]
    client_name: Optional[str]
    talent_id: Optional[str]
    talent_name: Optional[str]
    talent_grade: Optional[str]
    office_city: Optional[str]
    office_postal_code: Optional[str]
    booking_grade: Optional[str]
    industry: Optional[str]

    class Config:
        alias_generator = to_camel_case


class PlanningCreatedSchema(BaseModel):
    id: int
    original_id: str
    client_id: str
    talent_id: str
    office_id: Optional[int]
    job_manager_id: str
    operating_unit: str
    total_hours: float
    start_date: datetime.datetime
    end_date: datetime.datetime
    booking_grade: Optional[str]
    industry: Optional[str]
    is_unassigned: bool
    required_skills: List[SkillSchema]
    optional_skills: List[SkillSchema]

    class Config:
        orm_mode = True
