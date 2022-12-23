import datetime
from pydantic import BaseModel
from typing import Optional, List


class TalentSchema(BaseModel):
    id: Optional[str]
    name: Optional[str]
    grade: Optional[str]
