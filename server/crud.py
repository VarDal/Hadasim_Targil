from sqlalchemy.orm import Session
import models, schemas

def getHospitalMembers(db: Session):
    return db.query(models.HospitalMember).all()

def getHospitalMember(db: Session, id: int):
    return db.query(models.HospitalMember).filter(models.HospitalMember.id == id).first()

def createHospitalMember(db: Session, hospitalMember: schemas.HospitalMemberCreate):
    dbHospitalMember = models.HospitalMember(name=hospitalMember.name)
    db.add(dbHospitalMember)
    db.commit()
    db.refresh(dbHospitalMember)
    return dbHospitalMember

def deleteHospitalMember(id: int, db: Session):
    deletedMemberIndex = db.query(models.HospitalMember).filter(models.HospitalMember.id == id).delete()
    db.commit()
    return deletedMemberIndex

# לשנות שם של משתמש
