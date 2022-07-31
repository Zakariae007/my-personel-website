from bson import ObjectId
from schemas.experience import Experience
from database import connect_db

result_set = connect_db()
Experiences_collection = result_set.Experiences

def showExperience(experience) -> dict:
    return {
        "title": experience["title"],
        "type": experience["type"],
        "company" : experience["company"],
        "startDate" : experience["startDate"],
        "endDate" : experience["endDate"]
    }

async def add_new_experience(experience: Experience):
    experience = await Experiences_collection.insert_one(experience)
    new_experience = await Experiences_collection.find_one({"_id": experience.inserted_id})
    return showExperience(new_experience)

async def fetch_all_experience():
    experiences = []
    experiences_found = Experiences_collection.find()
    async for experience in experiences_found:
        experiences.append(showExperience(experience))
    return experiences

async def delete_experience(experience_id: str):
    found_experience = await Experiences_collection.find_one({"_id": ObjectId(experience_id)})
    if found_experience:
        experience = await Experiences_collection.delete_one({"_id": ObjectId(experience_id)})
        return experience

async def modify_experience(experience_id: str, experience: Experience):
    found_experience = await Experiences_collection.find_one({"_id": ObjectId(experience_id)})
    if found_experience: 
        modified_experience = await Experiences_collection.update_one({"_id": ObjectId(experience_id)}, {"$set": experience})
        return modified_experience