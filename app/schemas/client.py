import datetime
from pydantic import BaseModel
from typing import Optional, List


class ClientSchema(BaseModel):
    id: str
    name: Optional[str]
