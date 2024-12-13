from typing import Optional
from sqlmodel import Field, SQLModel


class SparePartUpdate(SQLModel):
    part_number: str | None = None
    name: str | None = None
    description: Optional[str] | None = None
    marca: Optional[str] | None = None
    qty: Optional[int] | None = None
