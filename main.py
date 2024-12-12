from typing import Optional

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, select
from routers import spare_parts

# Create the FastAPI app
app = FastAPI()

#Routers
app.include_router(spare_parts.router)

@app.get("/")
def read_root():
    return ("Hello World")


"""
# Create a Hero
@app.post("/heroes", response_model=Hero)
def create_hero(hero: Hero, session: Session = Depends(get_session)):
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero


# Read all heroes
@app.get("/heroes", response_model=list[Hero])
def read_heroes(
    skip: int = 0, limit: int = 10, session: Session = Depends(get_session)
):
    heroes = session.exec(select(Hero).offset(skip).limit(limit)).all()
    return heroes


# Read a hero by ID
@app.get("/heroes/{hero_id}", response_model=Hero)
def read_hero(hero_id: int, session: Session = Depends(get_session)):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


# Update a Hero
@app.put("/heroes/{hero_id}", response_model=Hero)
def update_hero(hero_id: int, hero_data: Hero, session: Session = Depends(get_session)):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")

    # Update the hero's attributes
    for field, value in hero_data.model_dump().items():
        setattr(hero, field, value)
    session.commit()
    session.refresh(hero)
    return hero


# Delete a Hero
@app.delete("/heroes/{hero_id}", response_model=Hero)
def delete_hero(hero_id: int, session: Session = Depends(get_session)):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")

    session.delete(hero)
    session.commit()
    return hero

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

"""

"""
from typing import Union
from fastapi import FastAPI


#APP Principal
app = FastAPI()


"""