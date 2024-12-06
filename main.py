from typing import Union
from fastapi import FastAPI
from routers import spare_parts

#APP Principal
app = FastAPI()

#Routers
app.include_router(spare_parts.router)

@app.get("/")
def read_root():
    return ("Hello World")