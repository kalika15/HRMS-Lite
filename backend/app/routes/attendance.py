from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import date
from app.database import get_db
from app.models.attendance import Attendance
from app.models.employee import Employee
from app.schemas.attendance import AttendanceCreate, AttendanceRead
from sqlalchemy import func


router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)

# Mark attendance
@router.post("/", response_model=AttendanceRead)
def mark_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db)
):
    # 1️⃣ Check employee exists (STRING comparison)
    employee = db.query(Employee).filter(
        Employee.employee_id == attendance.employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    # 2️⃣ Create attendance record
    new_attendance = Attendance(
        employee_id=attendance.employee_id,
        date=attendance.date,
        status=attendance.status
    )

    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)

    return new_attendance


# Get attendance records
@router.get("/debug/all")
def debug_attendance(db: Session = Depends(get_db)):
    return db.query(Attendance).all()

