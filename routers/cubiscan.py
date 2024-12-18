from fastapi import APIRouter, Depends, HTTPException
from database.schemas.cubiscan import Cubiscan
from database.schemas.cubiscan_update import CubiscanUpdate
from database.models.cubiscan import CubiscanPublic
from sqlmodel import Session, select, SQLModel
from database.sql_engine import get_session, engine


router = APIRouter(prefix="/cubiscan", tags=["Cubiscan"], responses={404 : {"message" : "No encontrado"}})

#Leer todos los equipos Cubiscan
@router.get("/", response_model=list[CubiscanPublic])
async def get_cubiscan(
    skip: int = 0,
    limit: int = 10,
    session: Session = Depends(get_session)
    ):
    cubiscan_db = session.exec(select(Cubiscan).offset(skip).limit(limit)).all()
    return(cubiscan_db)

#Agregar un "Cubiscan" al inventario
@router.post("/", response_model=CubiscanPublic)
def add_cubiscan(
    cubiscan: Cubiscan,
    session: Session = Depends(get_session), 
    ):
    SQLModel.metadata.create_all(engine)
    session.add(cubiscan)
    session.commit()
    session.refresh(cubiscan)
    return cubiscan

# Leer "Cubiscan" por "Serial Number"
@router.get("/{serial_number}", response_model=CubiscanPublic)
async def get_one_cubiscan(
    serial_number: str, 
    session: Session = Depends(get_session)
    ):
    cubiscan_db = session.exec(select(Cubiscan).where(Cubiscan.serial_number == serial_number)).first()
    if not cubiscan_db:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return cubiscan_db

# Actualizar uno o mas atributos de "Cubiscan"
@router.patch("/{serial_number}", response_model=CubiscanPublic)
async def update_cubiscan(serial_number : str, cubiscan : CubiscanUpdate, session: Session = Depends(get_session)):
    cubiscan_db = session.exec(select(Cubiscan).where(Cubiscan.serial_number ==serial_number)).first()
    if not cubiscan_db:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    cubiscan_data = cubiscan.model_dump(exclude_unset=True)
    cubiscan_db.sqlmodel_update(cubiscan_data)
    session.add(cubiscan_db)
    session.commit()
    session.refresh(cubiscan_db)
    return cubiscan_db

# Eliminar un "Cubiscan" de base de datos
# ******* SE ELIMINA DEFINITIVAMENTE *******************
@router.delete("/{serial_number}")
async def delete_cubiscan(serial_number : str, cubiscan : Cubiscan, session : Session = Depends(get_session)):
    cubiscan = session.exec(select(Cubiscan).where(Cubiscan.serial_number == serial_number)).first()
    if not cubiscan:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    session.delete(cubiscan)
    session.commit()
    return{"OK" : True} 
