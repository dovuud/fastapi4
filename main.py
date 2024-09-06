from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from typing import List
import models
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='resume FastAPI', description='FastAPI',desription='FastAPI for resume')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/about/', response_model=schemas.About)
async def create_about(data: schemas.AboutCreate,db: Session = Depends(get_db)):
    info = models.About(**data.dict())
    db.add(info)
    db.commit()
    db.refresh(info)
    return info

@app.get('/about-get/', response_model=List[schemas.About])
async def get_about(db: Session = Depends(get_db)):
    return db.query(models.About).all()

@app.post('/expirience/', response_model=schemas.Expirience)
async def create_expirience(expirience: schemas.ExpirienceCreate,db: Session = Depends(get_db)):
    exp = models.Expirience(**expirience.dict())
    db.add(exp)
    db.commit()
    db.refresh(exp)
    return exp

@app.get('/expirience-get/', response_model=List[schemas.About])
async def get_expirience(db: Session = Depends(get_db)):
    return db.query(models.Expirience).all()

@app.post('/education/', response_model=schemas.Education)
async def create_education(educ: schemas.EducationCreate,db: Session = Depends(get_db)):
    edu = models.Education(**educ.dict())
    db.add(edu)
    db.commit()
    db.refresh(edu)
    return edu

@app.get('/education-get/', response_model=List[schemas.Education])
async def get_education(db: Session = Depends(get_db)):
    return db.query(models.Education).all()
