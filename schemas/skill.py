from enum import Enum
from pydantic import BaseModel, Field

class Type(str, Enum):
    backend = "backend"
    frontend = "frontend"
    tool = "tool"

class Skill(BaseModel):
    name : str = Field(...)
    type : Type = Field(...)

class SkillCreate(Skill):
    name: str
    type: str

