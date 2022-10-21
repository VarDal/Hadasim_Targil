from sqlalchemy.orm import Session
import models, schemas

def getHospitalMembers(db: Session):
    return db.query(models.HospitalMember).all()

def getHospitalMember(db: Session, member_id: int):
    return db.query(models.HospitalMember).filter(models.HospitalMember.id == member_id).first()

def createHospitalMember(db: Session, hospitalMember: schemas.HospitalMemberCreate):
    dbHospitalMember = models.HospitalMember(name=hospitalMember.name)
    db.add(dbHospitalMember)
    db.commit()
    db.refresh(dbHospitalMember)
    return dbHospitalMember