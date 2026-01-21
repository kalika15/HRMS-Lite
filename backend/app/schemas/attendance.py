from pydantic import BaseModel
from datetime import date

# Schema for creating attendance
class AttendanceCreate(BaseModel):
    employee_id: str
    date: date
    status: str  # Present / Absent

# Schema for reading attendance
class AttendanceRead(BaseModel):
    id: int
    employee_id: str
    date: date
    status: str

    class Config:
        orm_mode = True
