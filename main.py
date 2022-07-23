from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import Admin, AdminUpdateRequest, Gender, Skill
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

app = FastAPI()

from adminRepository import (
    fetch_one_admin,
    fetch_all_admins,
    register_admin
)

from skillRepository import (
    fetch_all_skills,
    add_skill
)


origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

db: List[Admin] = [
    Admin(
        id= "62dbf33237547ddcc00ca9ba",
        firstName= "Zakariae", 
        lastName= "Barakat", 
        email= "Zakariae.barakat@gmail.com", 
        password= "Zakariae", 
        gender= Gender.male, 
    ),
    Admin(
        id= "96dbf33237547ddcc00ca9ba",
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

# Get all the admins
@app.get("/api/admins")
async def get_all_admins():
    admins = await fetch_all_admins()
    return admins

# Create a new admin
@app.post("/api/admins")
async def create_admin(admin: Admin):
    document = jsonable_encoder(admin)
    new_admin = await register_admin(document)
    if new_admin is not None: 
        return {"message": "User created successfully"}
    
    raise HTTPException(
        status_code= 404,
        detail= "could not create the admin"
    ) 

# Delete an existing admin
@app.delete("/api/admins/{admin_id}")
async def delete_admin(admin_id: UUID):
    for user in db:
        if user.id == admin_id:
            db.remove(user)
            return {"message": "user deleted successfully"}
    raise HTTPException(
        status_code= 404,
        detail= f"user with id: {admin_id} does not exists"
    )

# Update an existing admin
@app.put("/api/admins/{admin_id}")
async def update_admin(new_admin: AdminUpdateRequest, admin_id: UUID):
    for user in db:
        if user.id == admin_id:
            if new_admin.firstName is not None:
                user.firstName = new_admin.firstName
            if new_admin.lastName is not None:
                user.lastName = new_admin.lastName
            if new_admin.email is not None:
                user.email = new_admin.email
            if new_admin.password is not None:
                user.password = new_admin.password
            if new_admin.gender is not None:
                user.gender = new_admin.gender
            return {"message": "user updated successfully"}

    raise HTTPException(
        status_code= 404,
        detail= f"user with id: {admin_id} does not exists"
    )

# Get specific admin
@app.get("/api/admins/{admin_id}")
async def get_admin_by_id(admin_id: str):
    response = await fetch_one_admin(admin_id)
    if response:
        return response

    raise HTTPException(
        status_code= 404,
        detail= f"user with id: {admin_id} does not exists"
    )

@app.get("/api/skills")
async def get_all_skills():
    response = await fetch_all_skills()
    return response

@app.post("/api/skills")
async def add_new_skill(skill: Skill):
    document = jsonable_encoder(skill)
    new_skill = await add_skill(document)

    if new_skill is not None: 
        return {"message": "Skill added successfully"}
    
    raise HTTPException(
        status_code= 404,
        detail= "could not add the skill"
    ) 

