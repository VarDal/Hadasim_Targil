from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

import database

class HospitalMember(database.Base):
    __tablename__ = "hospital_members"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, unique=False)
    sickDate = Column(DateTime)
    vaccineDate = Column(DateTime)
    recoveryDate = Column(DateTime)