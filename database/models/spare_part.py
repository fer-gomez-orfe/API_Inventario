from typing import Optional
from pydantic import BaseModel


class SparePartPublic(BaseModel):
    item_Eng: str
    item_Esp: str
    description: Optional[str] = None
    serial_number: Optional[str] = None
    ult_actualizacion: Optional[str] = None
    cantidad: Optional[int] = None
    notas: Optional[str] = None
    part_number: Optional[str] = None

