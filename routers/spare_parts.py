from fastapi import APIRouter, Depends, HTTPException, status
from database.schemas.spare_part import SparePart
from database.models.spare_part import SparePartModel
from sqlmodel import Session, select
from database.sql_engine import get_session


router = APIRouter(prefix="/spare_parts", tags=["spare_parts"], responses={404 : {"message":"No encontrado"}})

#Read all spare parts
@router.get("/", response_model=list[SparePartModel])
async def spare_parts(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    spare_parts = session.exec(select(SparePart).offset(skip).limit(limit)).all()
    return(spare_parts)

# Create a spare part
@router.post("/", response_model=SparePart)
def create_hero(spare_part: SparePart, session: Session = Depends(get_session)):
    session.add(spare_part)
    session.commit()
    session.refresh(spare_part)
    return spare_part

# Read a SparePart by ID
@router.get("/{part_number}", response_model=SparePart)
def read_hero(part_number: str, session: Session = Depends(get_session)):
    spare_part = session.exec(select(SparePart).where(SparePart.part_number == part_number)).first()
    if not spare_part:
        raise HTTPException(status_code=404, detail="Spare Part not found")
    return spare_part
