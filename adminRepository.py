from schemas.admin import Admin
from database import connect_db
from bson.objectid import ObjectId

result_set = connect_db()
admin_collection = result_set.Admin

def admin_helper(admin) -> dict:
    return {
        "id": str(admin["_id"]),
        "firstName": admin["firstName"],
        "lastName": admin["lastName"],
        "email": admin["email"],
        "password": admin["password"],
        "gender": admin["gender"],
    }

# Find an admin by ID
async def fetch_one_admin(id):
    document = await admin_collection.find_one({"_id": ObjectId(id)})
    return admin_helper(document)

# Get all the admins
async def fetch_all_admins():
    admins = []
    admins_found = admin_collection.find() 
    async for admin in admins_found:
        admins.append(admin_helper(admin))
    return admins

async def register_admin(admin):
    inserted_admin = await admin_collection.insert_one(admin)
    new_admin = await admin_collection.find_one({"_id": inserted_admin.inserted_id})
    return admin_helper(new_admin)

#update document should be implemented
async def modify_admin(id, data):
    existing_admin = await admin_collection.find_one({"_id": ObjectId(id)})
    if existing_admin:
        updated_admin = await admin_collection.update_one({"id": ObjectId(id)}, {"$set": data})
        print("Updated admin : ", updated_admin)
        return updated_admin

async def delete_admin(id):
    found_admin = await admin_collection.find_one({"_id": ObjectId(id)})
    if found_admin:
        admin = await admin_collection.delete_one({"_id": ObjectId(id)})
        return admin

    

    

