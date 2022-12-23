import datetime
from pydantic import BaseModel
from typing import Optional, List


class OfficeSchema(BaseModel):
    id: Optional[int]
    city: Optional[str]
    postal_code: str
