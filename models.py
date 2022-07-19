from datetime import date
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr, Field
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Admin(BaseModel):
    id: Optional[UUID] = uuid4()
    firstName : str = Field(...)
    lastName : str = Field(...)
    email : EmailStr = Field(...)
    password: str = Field(...)
    gender: Gender = Field(...)

class AdminUpdateRequest(BaseModel):
    firstName : Optional[str]
    lastName : Optional[str]
    email : Optional[EmailStr]
    password: Optional[str]
    gender: Optional[Gender]

class skill(BaseModel):
    name : str = Field(...)
    skillType : str = Field(...)

class experience(BaseModel):
    title : str = Field(...) 
    company : str = Field(...)
    startDate : date = Field(...)
    endDate : date = Field(...)
    period : str = Field(...)
    description : str = Field(...)
    skills: str = Field(...)