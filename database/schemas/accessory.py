from sqlmodel import Field, SQLModel

class Accessory(SQLModel, table= True):
    id: int | None= Field(default=None, primary_key= True)
    serial_number: str
    name: str
    description: str