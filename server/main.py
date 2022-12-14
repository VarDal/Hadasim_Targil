from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import crud
import models
import database
import schemas
from fastapi.middleware.cors import CORSMiddleware


models.database.Base.metadata.create_all(bind=database.engine)

app=FastAPI()#מכיל את כל נתוני האפליקציה

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.delete('/{id}')
def deleteCovidPatient(id: int,  db: Session = Depends(get_db)):
    if crud.getHospitalMember(db,id) is None:
        return None
    return crud.deleteHospitalMember(id,db)

@app.put('/{id}')
def UpdateNameMember(id:int, member: schemas.HospitalMemberCreate, db: Session = Depends(get_db)):
    if crud.getHospitalMember(db,id) is None:
        return None
    return crud.updateNameMember(db,id,member.name)
    

