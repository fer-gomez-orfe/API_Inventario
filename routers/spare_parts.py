from fastapi import APIRouter, Depends, HTTPException, status
from database.schemas.spare_part import SparePart
from database.models.spare_part import SparePartModel
from sqlmodel import Session, select
from database.schemas.spare_part_update import SparePartUpdate
from database.sql_engine import get_session


router = APIRouter(prefix="/spare_parts", tags=["spare_parts"], responses={404 : {"message":"No encontrado"}})

# Leer todas las "Spare Parts"
@router.get("/", response_model=list[SparePartModel])
async def spare_parts(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    spare_parts = session.exec(select(SparePart).offset(skip).limit(limit)).all()
    return(spare_parts)

# Agregar un "Spare Part"
@router.post("/", response_model=SparePartModel)
def create_hero(spare_part: SparePart, session: Session = Depends(get_session)):
    session.add(spare_part)
    session.commit()
    session.refresh(spare_part)
    return spare_part

# Leer "SparePart" por "Part Number"
@router.get("/{part_number}", response_model=SparePartModel)
def read_hero(part_number: str, session: Session = Depends(get_session)):
    spare_part = session.exec(select(SparePart).where(SparePart.part_number == part_number)).first()
    if not spare_part:
        raise HTTPException(status_code=404, detail="Pieza no encontrada")
    return spare_part

# Actualizar uno o mas atributos de "SparePart"
@router.patch("/{part_number}", response_model=SparePartModel)
def update_spare_part(part_number : str, spare_part : SparePartUpdate, session: Session = Depends(get_session)):
    spare_part_db = session.exec(select(SparePart).where(SparePart.part_number == part_number)).first()
    if not spare_part_db:
        raise HTTPException(status_code=404, detail="Pieza no encontrada")
    spare_part_data = spare_part.model_dump(exclude_unset=True)
    spare_part_db.sqlmodel_update(spare_part_data)
    session.add(spare_part_db)
    session.commit()
    session.refresh(spare_part_db)
    return spare_part_db

# Eliminar un "Spare Part" de base de datos
# ******* SE ELIMINA DEFINITIVAMENTE *******************
@router.delete("/{part_number}")
def delete_spare_part(part_number : str, spare_part : SparePart, session : Session = Depends(get_session)):
    spare_part = session.exec(select(SparePart).where(SparePart.part_number == part_number)).first()
    if not spare_part:
        raise HTTPException(status_code=404, detail="Pieza no encontrada")
    session.delete(spare_part)
    session.commit()
    return{"OK" : True} 

