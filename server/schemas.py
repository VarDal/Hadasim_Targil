from datetime import  datetime
from pydantic import BaseModel


class HospitalMemberBase(BaseModel):
    name: str
    sickDate: datetime | None = None
    vaccineDate : datetime | None = None
    recoveryDate : datetime | None = None

class HospitalMemberCreate(HospitalMemberBase):
    pass

class HospitalMember(HospitalMemberBase):
    id: int
    class Config:
        orm_mode = True