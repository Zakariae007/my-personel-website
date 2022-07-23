from models import Skill
from database import connect_db

result_set = connect_db()
Skills = result_set.Skills

# Get all skills 
async def fetch_all_skills():
    skills = await Skills.find().to_list(100)
    return skills

async def add_skill(skill):
    new_skill = await Skills.insert_one(skill)
    return new_skill

