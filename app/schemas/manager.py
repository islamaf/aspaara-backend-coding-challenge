import datetime
from pydantic import BaseModel
from typing import Optional, List


class JobManagerSchema(BaseModel):
    id: Optional[str]
    name: Optional[str]
