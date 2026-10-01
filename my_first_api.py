from pydantic import BaseModel, Field, field_validator
from fastapi import FastAPI
from fastapi import FastAPI, status, HTTPException

from typing import Optional


class UserCV(BaseModel):
    
    name: str = Field(min_lenght=3)
    email: str
    expected_salary: int= Field(gt=0)
    is_remote: bool = True
    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Email must contain @ symbol!")
        return value
fake_cv_db = []
print("🚀 Starting the Backend Server...")



app = FastAPI()


@app.get("/")
def home():
    return{"message":"Welcome to my first API!"}
    
@app.get("/developer")
def developer_info():
    return {"name": "Your Name", "target_role": "Python Backend Developer", "target_salary": "1 Lakh BDT"}



@app.get("/salary/{experience_level}")
def check_salary(experience_level: str):
    
    
    if experience_level == "junior":
        return {"experience": "0-1 Years", "expected_salary": "20k-30k BDT", "status": "Learning Phase"}
    
    elif experience_level == "mid":
        
        return {"experience": "2-3 Years", "expected_salary": "65k-1 Lakh BDT", "status": "Do or Die Target"}
    
    elif experience_level == "senior":
        return {"experience": "5+ Years", "expected_salary": "1.5L-3L BDT", "status": "Architecture Master"}
    
    else:
        return {"error": "Level not found. Please use 'junior', 'mid', or 'senior' in the URL."}
    
@app.get("/jobs")
def check_jobs(title: str="developer", location:str="dhaka"):
    if title=="backend" and location == "remote":
        return {"job_role": "Python Backend Engineer", "salary": "80k-1L BDT", "type": "Remote", "status": "Dream Job Unlocked"}
    else:
        return {"message": f"Searching for {title} jobs in {location}..."}

@app.get("/search-jobs/{job_type}")
def customer_search(job_type: str, location: str= "dhaka"):
    if job_type == "backend" and location == "remote":
        return {"status": "Jackpot! Remote backend job found."}
    else:
        return {"message": f"Looking for {job_type} roles in {location}..."}

@app.get("/find-job")
def find_job(title:str, location: Optional[str]= None):
    if location:
        return{"message": f"Searching for {title} jobs in {location}..."}
    else:
        return {"message": f"Searching for {title} jobs EVERYWHERE! "}
    
@app.post("/submit-cv", status_code=status. HTTP_201_CREATED)
def submit_cv(cv: UserCV):
    fake_cv_db.append(cv.model_dump())
    return {"message": f"CV successfully received for {cv.name}", "salary_demand": cv.expected_salary, "remote_status": cv.is_remote}

@app.get("/all-cvs")
def get_all_cvs():
    return {"total_cvs": len(fake_cv_db), "database": fake_cv_db}

@app.get ("/cv/{user_email}")
def get_single_cv (user_email:str):
    for cv in fake_cv_db:
        if cv ["email"]== user_email:
            return cv
    raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail= f" no cv found for this email: {user_email} ")