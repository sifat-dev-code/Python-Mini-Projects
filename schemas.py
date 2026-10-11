from pydantic import BaseModel, Field, field_validator
from typing import  List


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