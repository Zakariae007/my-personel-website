from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Admin(BaseModel):
    id: Optional[UUID] = uuid4()
    firstName : str
    lastName : str
    email : str
    password: str
    gender: Gender