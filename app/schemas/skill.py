import datetime
from pydantic import BaseModel
from typing import Optional, List


class SkillSchema(BaseModel):
    name: str
    category: str
