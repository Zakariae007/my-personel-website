from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Admin, Gender

app = FastAPI()

db: List[Admin] = [
    Admin(
        id= uuid4(),
        firstName= "Zakariae", 
        lastName= "Barakat", 
        email= "Zakariae.barakat@gmail.com", 
        password= "Zakariae", 
        gender= Gender.male, 
    ),
    Admin(
        id= uuid4(),
        firstName= "test", 
        lastName= "test", 
        email= "test@gmail.com", 
        password= "test", 
        gender= Gender.female, 
    )
]

@app.get("/")
def root(): 
    return {"hello" : "world"}

@app.get("/admins")
def root(): 
    return db