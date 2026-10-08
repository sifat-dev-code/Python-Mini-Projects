from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, Field, field_validator
from typing import  List
from sqlalchemy.orm import Session
from database import get_db
from models import DBCV


router = APIRouter()
class Experience(BaseModel):
    company : str
    role : str
    years : int 


class UserCV(BaseModel):
    
    name: str = Field(min_lenght=3)
    email: str
    expected_salary: int= Field(gt=0)
    is_remote: bool = True
    skills : List[str] = []
    experience : List[Experience] = []

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Email must contain @ symbol!")
        return value
fake_cv_db = []

@router.post("/submit-cv", status_code=status. HTTP_201_CREATED)
def submit_cv(cv: UserCV, db: Session=Depends(get_db)):
    
    #fake_cv_db.append(cv.model_dump())
    #return {"message": f"CV successfully received for {cv.name}", "salary_demand": cv.expected_salary, "remote_status": cv.is_remote}

    new_cv = DBCV(
    name= cv.name,
    email=cv.email,
    expected_salary=cv.expected_salary,
    is_remote=cv.is_remote   
)
    db.add(new_cv)
    db.commit()    
    db.refresh(new_cv)
    return {"message": "CV Successfully Saved in Database!", "cv_id": new_cv.id}
@router.get("/all-cvs")
def get_all_cvs(db : Session=Depends(get_db)):
    all_record = db.query(DBCV).all()
    return {"total_cvs": len(all_record), "database": all_record}

@router.get ("/cv/{user_email}")
def get_single_cv (user_email:str):
    for cv in fake_cv_db:
        if cv ["email"]== user_email:
            return cv
    raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail= f" no cv found for this email: {user_email} ")

@router.delete ("/cv/{user_email}")
def delete_cv (user_email:str):
    for cv in fake_cv_db:
        if cv["email"]== user_email:
            fake_cv_db.remove(cv)
            return {"message": f"CV for {user_email} deleted successfully!"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Data Not Found")


@router.put("/cv/{user_email}")
def updated_cv (user_email : str, new_cv : UserCV):
    for cv in fake_cv_db:
        if cv["email"] == user_email:
            cv.update(new_cv.model_dump())
            return {"Messege": f"CV for {user_email} Updated Successfully"}
    raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail= "CV not found")

@router.get("/search-cvs")
def search_cvs (remote_only : bool =True, max_salary: int = 100000):
    matched_cvs=[]
    for cv in fake_cv_db:
        if cv["is_remote"] == remote_only and cv ["expected_salary"]<=  max_salary:
            matched_cvs.append(cv)
    return matched_cvs
    
        
