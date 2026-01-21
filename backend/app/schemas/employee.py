from pydantic import BaseModel, EmailStr

# Schema for creating an employee
class EmployeeCreate(BaseModel):
    employee_id: str
    full_name: str
    email: EmailStr
    department: str

# Schema for reading employee data (response)
class EmployeeRead(BaseModel):
    id: int
    employee_id: str
    full_name: str
    email: EmailStr
    department: str

    class Config:
        orm_mode = True
