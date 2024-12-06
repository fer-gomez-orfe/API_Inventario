from pydantic import BaseModel
from typing import Optional

class SparePart(BaseModel):
    id: Optional[str] = None
    part_number : str
    name: str
    description: str
    marca: str
    qty: int
    