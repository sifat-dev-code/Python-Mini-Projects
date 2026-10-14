from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import DBCV, User
from schemas import UserCV, Experience, UserCreate
import bcrypt
from datetime import datetime, timedelta,timezone
from jose import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError

SECRET_KEY = "sifat_super_secret_key_banna_123" 
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
def get_current_user(token:str=Depends(oauth2_scheme), db:Session =Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms= [ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    except JWTError:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    user = db.query(User).filter(User.email==email).first()
    if user is None:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    return user
def create_access_token(data: dict):
    to_encode = data.copy()

    
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_password_hash(password: str):
    pwd_bytes = password.encode('utf-8')
    hashed_bytes = bcrypt.hashpw(pwd_bytes, bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')
def verify_password(plain_password: str, hashed_password: str):
    
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

router = APIRouter()

fake_cv_db = []

@router.post("/submit-cv", status_code=status. HTTP_201_CREATED)
def submit_cv(cv: UserCV, db: Session=Depends(get_db), current_user= Depends(get_current_user)):
    
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

@router.post("/register")
def register_user(user_data: UserCreate, db: Session=Depends(get_db)):
     reg_user = db.query(User).filter(User.email==user_data.email).first()
     if reg_user :
          raise HTTPException (status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered") 
     hash_pwd = get_password_hash(user_data.password)
     user_reg = User(
          email = user_data.email,
          hashed_password = hash_pwd
     )
     db.add(user_reg)
     db.commit()
     db.refresh(user_reg)
     return {"message": "User created successfully", "email": user_data.email}
@router.post("/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
     reg_user = db.query(User).filter(User.email==form_data.username).first()
     if not reg_user:
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
     log_pass = verify_password(form_data.password,reg_user.hashed_password)
     if log_pass is False:
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
     access_token = create_access_token(data={"sub": form_data.username})
     return {"access_token": access_token, "token_type": "bearer"}





    
