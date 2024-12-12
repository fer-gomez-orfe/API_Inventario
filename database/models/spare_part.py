from typing import Optional
from pydantic import BaseModel


class SparePartModel(BaseModel):
    id: Optional[int] = None
    part_number: str
    name: str
    description: Optional[str] = None
