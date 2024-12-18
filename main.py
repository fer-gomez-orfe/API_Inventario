from typing import Optional

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, select
from routers import spare_parts, cubiscan

# Create the FastAPI app
app = FastAPI()

#Routers
app.include_router(spare_parts.router)
app.include_router(cubiscan.router)

@app.get("/")
def read_root():
    return ("Hello World")
