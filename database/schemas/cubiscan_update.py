from sqlmodel import SQLModel

class CubiscanUpdate(SQLModel):
    serial_number: str | None = None
    model: str | None = None
    description: str | None = None