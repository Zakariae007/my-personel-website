from datetime import date
from typing import Optional
from uuid import UUID, uuid4
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
 
class Skill(BaseModel):
    name : str = Field(...)
    type : str = Field(...)

class Experience(BaseModel):
    title : str = Field(...) 
    company : str = Field(...)
    startDate : date = Field(...)
    endDate : date = Field(...)
    period : str = Field(...)
    description : str = Field(...)
    skills: str = Field(...)