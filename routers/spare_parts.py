from fastapi import APIRouter, HTTPException, status
from database.models.spare_part import SparePart
from database.mongo_client import db_client
from database.schemas.spare_part import spare_parts_schema


router = APIRouter(prefix="/spare_part", tags=["spare_parts"], response={404 : {"message":"No encontrado"}})

#GET
@router.get("/", response_model = list[SparePart])
async def spare_parts():
    return spare_parts_schema(db_client.spare_part.find())

