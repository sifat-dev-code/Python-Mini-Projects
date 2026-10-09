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



@router.delete ("/cv/{cv_id}")
def delete_cv (cv_id:int, db:Session=Depends(get_db)):
    cv_to_delete = db.query(DBCV).filter(DBCV.id==cv_id).first()
    
    if cv_to_delete is None:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail= "CV not found")
    db.delete(cv_to_delete)
    db.commit()
    return {"message": "CV Deleted Successfully"}
            
    

@router.put("/cv/{cv_id}")
def updated_cv (cv_id : int, updated_data:UserCV, db : Session= Depends(get_db)):
    cv_to_update = db.query(DBCV).filter(DBCV.id==cv_id).first()
    if cv_to_update is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "CV not found")
    cv_to_update.name = updated_data.name
    cv_to_update.email = updated_data.email
    cv_to_update.expected_salary= updated_data.expected_salary
    cv_to_update.is_remote=updated_data.is_remote
    db.commit()
    db.refresh(cv_to_update)
    return cv_to_update

    
            
    

@router.get("/search-cvs")
def search_cvs (remote_only : bool =True, max_salary: int = 100000):
    matched_cvs=[]
    for cv in fake_cv_db:
        if cv["is_remote"] == remote_only and cv ["expected_salary"]<=  max_salary:
            matched_cvs.append(cv)
    return matched_cvs
    
@router.get("/cv/{cv_id}")
def get_single_CV(cv_id:int, db: Session=Depends(get_db)):
    single_cv = db.query(DBCV).filter(DBCV.id==cv_id).first()
    if single_cv is None:
            raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail= "CV not found")      

    return single_cv
        
    
