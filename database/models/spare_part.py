from typing import Optional
from pydantic import BaseModel


class SparePartPublic(BaseModel):
    part_number: str
    name: str
    description: Optional[str] = None
