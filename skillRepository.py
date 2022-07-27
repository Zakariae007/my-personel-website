from models import Skill
from database import connect_db

result_set = connect_db()
Skills = result_set.Skills

# Get all skills 
async def fetch_all_skills():
    skills = await Skills.find().to_list(100)
    return skills

# Add new skills 
async def add_skill(skill):
    new_skill = await Skills.insert_one(skill)
    return new_skill

async def delete_skill(skill_id):
    deleted_skill = await Skills.delete_one(skill_id)
    return deleted_skill
