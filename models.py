from sqlalchemy import Column, Integer, String, Boolean
from database import Base 

class DBCV(Base):
    __tablename__ = "cv_records"
    id = Column(Integer, primary_key= True, index= True)
    name = Column(String)
    email = Column (String, unique= True)
    expected_salary = Column(Integer)
    is_remote = Column(Boolean, default=True)
    
class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index= True)
    hashed_password = Column(String)