from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import DBCV
from schemas import UserCV, Experience


router = APIRouter()





   
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
def get_all_cvs(db : Session=Depends(get_db), skip:int=0, limit:int=10):
    total_cv = db.query(DBCV).count()
    if limit>total_cv:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "You reached your limit")
    all_record = db.query(DBCV).offset(skip).limit(limit).all()
    
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
def search_cvs (remote_only : bool =True, max_salary: int = 100000, db:Session = Depends(get_db)):
    result = db.query(DBCV).filter(DBCV.is_remote==remote_only,DBCV. expected_salary <= max_salary).all()
    return result
    
    
@router.get("/cv/{cv_id}")
def get_single_CV(cv_id:int, db: Session=Depends(get_db)):
    single_cv = db.query(DBCV).filter(DBCV.id==cv_id).first()
    if single_cv is None:
            raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail= "CV not found")      

    return single_cv
        
    
