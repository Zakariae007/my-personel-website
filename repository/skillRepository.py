from bson import ObjectId
from schemas.skill import Skill, SkillCreate
from database import connect_db

result_set = connect_db()
skill_collection = result_set.Skills

def showSkill(skill: Skill) -> dict:
    return {
        "id": str(skill["_id"]),
        "name": skill["name"],
        "type": skill["type"]
    }

# Get all skills 
async def fetch_all_skills():
    skills = []
    found_skills = skill_collection.find()
    async for skill in found_skills:
        skills.append(showSkill(skill))
    return skills

# Add new skills 
async def add_skill(skill: SkillCreate):
    new_skill = await skill_collection.insert_one(skill)
    return new_skill

# delete an existing skill
async def delete_skill(skill_id):
    found_skill = await skill_collection.find_one({"_id": ObjectId(skill_id)})
    if found_skill:
        skill = await skill_collection.delete_one({"_id": ObjectId(skill_id)})
        return skill
