from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
from schemas.skill import Skill
from schemas.admin import Admin, Gender
from schemas.experience import Experience
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

app = FastAPI()

from repository.adminRepository import (
    fetch_one_admin,
    fetch_all_admins,
    register_admin,
    modify_admin,
    delete_admin
)

from repository.skillRepository import (
    fetch_all_skills,
    add_skill,
    delete_skill
)

from repository.experienceRepository import (
    add_new_experience,
    fetch_all_experience,
    delete_experience,
    modify_experience
)


origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# db: List[Admin] = [
#     Admin(
#         id= "62dbf33237547ddcc00ca9ba",
#         firstName= "Zakariae", 
#         lastName= "Barakat", 
#         email= "Zakariae.barakat@gmail.com", 
#         password= "Zakariae", 
#         gender= Gender.male, 
#     ),
#     Admin(
#         id= "96dbf33237547ddcc00ca9ba",
#         firstName= "test", 
#         lastName= "test", 
#         email= "test@gmail.com", 
#         password= "test", 
#         gender= Gender.female, 
#     )
# ]

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

# Update an existing admin
@app.put("/api/admins/{admin_id}")
async def update_admin( admin_id: str, admin: Admin):
    new_admin = await modify_admin(admin_id, admin)
    if new_admin: 
        return new_admin

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

# delete an admin
@app.delete("/api/admins/{admin_id}")
async def delete_existing_admin(admin_id: str):
    response = await delete_admin(admin_id)
    if response:
        return {"message": "user deleted successfully"}

    raise HTTPException(
        status_code= 404,
        detail= f"user with id: {admin_id} does not exists"
    )

# Get all skills
@app.get("/api/skills")
async def get_all_skills():
    response = await fetch_all_skills()
    return response

# Add a new skill
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

# Delete a skill
@app.delete("/api/skills/{skill_id}")
async def delete_existing_skill(skill_id: str):
    response = await delete_skill(skill_id)
    if response is not None:
        return {"message": "Skill was deleted successfully"}

    raise HTTPException(
        status_code= 404,
        detail= "could not delete the skill"
    ) 

# Add new experience
@app.post("/api/experience")
async def create_experience(experience: Experience):
    document = jsonable_encoder(experience)
    new_experience = await add_new_experience(document)

    if new_experience is not None: 
        return {"message": "Experience added successfully"}
    
    raise HTTPException(
        status_code= 404,
        detail= "could not add the experience"
    ) 

# Get all experiences
@app.get("/api/experience")
async def get_all_experience():
    experiences = await fetch_all_experience()
    return experiences

# Delte an existing experience
@app.delete("/api/experience")
async def delete_existing_experience(experience_id: str):
    experience = await delete_experience(experience_id)
    if experience is not None:
        return {"message": "Experience was deleted successfully"}

    raise HTTPException(
        status_code= 404,
        detail= "could not delete the experience"
    )

# Update an existing experience
@app.put("/api/experience/{experience_id}")
async def delete_existing_experience(experience_id: str, data: Experience):
    experience = await modify_experience(experience_id, data)
    if experience is not None:
        return {"message": "Experience was updated successfully"}

    raise HTTPException(
        status_code= 404,
        detail= "could not update the experience"
    )


