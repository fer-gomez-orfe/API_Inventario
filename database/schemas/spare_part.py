from typing import Optional
from sqlmodel import Field, SQLModel


class SparePart(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    part_number: str
    name: str
    description: str = None
    marca: str = None
    qty: int = None
