from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI
from models import Admin, Gender

app = FastAPI()

db: List[Admin] = [
    Admin(
        id= UUID("c55cca20-f511-49b7-9df7-81fea762d5bf"),
        firstName= "Zakariae", 
        lastName= "Barakat", 
        email= "Zakariae.barakat@gmail.com", 
        password= "Zakariae", 
        gender= Gender.male, 
    ),
    Admin(
        id= UUID("90c1f42d-4cd4-4aac-ab9b-a14b2b6deb52"),
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

@app.get("/api/admins")
async def get_all_admins(): 
    return db;

@app.post("/api/admins")
async def register_admin(admin: Admin): 
    db.append(admin)
    return {"id": admin.id}

@app.delete("/api/admins/{admin_id}")
async def delete_admin(admin_id: UUID):
    for user in db:
        if user.id == admin_id:
            db.remove(user)
            return {"message": "user deleted successfully"}

    return {"message": "could not find user with this id"}