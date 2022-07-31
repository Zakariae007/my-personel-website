from datetime import date
from enum import Enum
from pydantic import BaseModel, Field

class Type(str, Enum):
    internship = "internship"
    parttime = "parttime"
    fulltime = "fulltime"

class Experience(BaseModel):
    title : str = Field(...)
    type : Type = Field(...)
    company : str = Field(...)
    startDate : date = Field(...)
    endDate : date = Field(...)


class createdExperience(Experience):
    title: str
    type: Type
    company : str
    startDate: date
    endDate: date

