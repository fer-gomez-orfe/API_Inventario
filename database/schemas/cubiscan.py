from typing import Optional
from sqlmodel import Field, SQLModel


class Cubiscan(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    serial_number: str
    model: str
    description: str