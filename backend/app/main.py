from fastapi import FastAPI
from app.routes import employee, attendance
from app.database import init_db

init_db()

app = FastAPI(title="HRMS Lite")

app.include_router(employee.router)
app.include_router(attendance.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to HRMS Lite API"}
@app.get("/api/health")
def health():
    return {"status": "ok"}