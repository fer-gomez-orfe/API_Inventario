from sqlmodel import Field, SQLModel


class SparePart(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    item_Eng: str| None = None
    item_Esp: str| None = None
    description: str| None = None
    serial_number: str| None = None
    pedimento: int | None = None
    ult_actualizacion: str| None = None
    cantidad: int| None = None
    notas: str| None = None
    part_number: str| None = None
    part_number_montra: str| None = None
    ubicacion : str| None = None
    costo_compra_usd : float| None = 0.0
    costo_venta_profit_usd : float| None = 0.0
    costo_compra_mxn : float| None = 0.0
    costo_venta_profit_mxn : float| None = 0.0
    largo : float| None = None
    ancho : float| None = None
    alto : float| None = None
    peso : float| None = None
    lugar_origen : str| None = None
