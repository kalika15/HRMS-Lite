from app.database import Base, engine

# 👇 THIS IS REQUIRED
from app.models.employee import Employee
from app.models.attendance import Attendance

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
