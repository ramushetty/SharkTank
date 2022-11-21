from fastapi import FastAPI
import uuid
from uuid import UUID
from pydantic import BaseModel
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Pitch_Schema(BaseModel):
    entrepreneur: str
    pitchTitle: str
    pitchIdea: str
    askAmount: float
    equity: float 

    class Config:
        orm_mode = True

class Pitch_Offer_Schema(BaseModel):
    investor: str
    comment: str
    amount: float
    equity: float 

    class Config:
        orm_mode = True


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/pitches")
async def create_pitches(pitch: Pitch_Schema,db: Session = Depends(get_db)):
    pitch = models.Pitch(**pitch.dict())
    db.add(pitch)
    db.commit()
    db.refresh(pitch)
    return pitch.id
@app.get("/pitches")
async def get_pitches(db: Session = Depends(get_db)):
    return db.query(models.Pitch).all()


@app.post("/pitches/{pitch_id}/makeOffer")
async def pitches(pitch_id: UUID,pitch_offer_schema:Pitch_Offer_Schema, db: Session = Depends(get_db)):
    str_pitch_id = str(pitch_id)
    print(str_pitch_id)
    if db.query(models.Pitch).filter(models.Pitch.id==str_pitch_id).first() is None:
        raise HTTPException(status_code=404, detail="Pitch ID not found")
    pitch_offer = models.Pitch_Offer(**pitch_offer_schema.dict(), pitch_id=str(pitch_id))
    db.add(pitch_offer)
    db.commit()
    db.refresh(pitch_offer)
    return pitch_offer.id
        