from msilib import schema
from unicodedata import name
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session
import crud
import models
import database
import schemas


models.database.Base.metadata.create_all(bind=database.engine)

app=FastAPI()#מכיל את כל נתוני האפליקציה

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def GetCovidPatients(db: Session = Depends(get_db)):
    return crud.getHospitalMembers(db)

@app.get('/{id}')
def GetCovidPatient(id: int, db: Session = Depends(get_db)):
   return crud.getHospitalMember(db, id)
   
@app.post("/", response_model=schemas.HospitalMember)
def addCovidPatient(member: schemas.HospitalMemberCreate,  db: Session = Depends(get_db)):
    return crud.createHospitalMember(db, member)

# @app.delete('/{name}')
# def deleteCovidPatient(name: str,  db: Session = Depends(get_db)):
#     if covidPatients.__contains__(name):
#         covidPatients.remove(name)
#         return name
#     return None

# @app.put('/{name}')
# def UpdateCovidPatient(name: str, patient: Patient, db: Session = Depends(get_db)):
#     for covidPatientIndex, covidPatient in enumerate(covidPatients):
#         if covidPatient == name:
#             covidPatients[covidPatientIndex] = patient.name
#             return patient.name
#     return None

