from models import Admin
from database import connect_db

result_set = connect_db()
admin_collection = result_set.Admin

# Find an admin by ID
async def fetch_one_admin(id):
    document = await admin_collection.find_one({"_id": id})
    return document

# Get all the admins
async def fetch_all_admins():
    admins = await admin_collection.find().to_list(10) #10 is just a random number, since to_list needs an argument which is the length
    return admins

async def register_admin(admin):
    new_admin = await admin_collection.insert_one(admin)
    return new_admin

#update document should be implemented
# async def update_admin(id, admin):
    # payload = {}
    # old_admin = await admin_collection.find_one({"_id": id})
    # await admin_collection.update_one({"id": id}, )

