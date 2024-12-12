from typing import Optional
from sqlmodel import Field, SQLModel


class SparePart(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    part_number: str
    name: str
    description: Optional[str] = None
    marca: Optional[str] = None
    qty: Optional[int] = None
