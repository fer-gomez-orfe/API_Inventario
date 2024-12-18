from pydantic import BaseModel
from typing import Optional

class CubiscanPublic(BaseModel):
    serial_number: str
    model: str

