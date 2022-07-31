from pydantic import BaseModel, EmailStr, Field
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Admin(BaseModel):
    firstName : str = Field(...)
    lastName : str = Field(...)
    email : EmailStr = Field(...)
    password: str = Field(...)
    gender: Gender = Field(...)