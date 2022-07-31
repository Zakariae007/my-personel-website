from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class Experience(BaseModel):
    title : str = Field(...) 
    company : str = Field(...)
    startDate : date = Field(...)
    endDate : date = Field(...)
    period : str = Field(...)
    description : str = Field(...)
    skills: str = Field(...)