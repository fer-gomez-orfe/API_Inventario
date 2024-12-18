from typing import Optional
from sqlmodel import Field, SQLModel


class SparePartUpdate(SQLModel):
    part_number: str | None = None
    name: str | None = None
    description: str | None = None
    marca: str | None = None
    qty: int | None = None
