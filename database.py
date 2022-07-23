from models import Admin
import os
from dotenv import load_dotenv

import motor.motor_asyncio 
load_dotenv()

connection_string = os.getenv('DB_URL')

client = motor.motor_asyncio.AsyncIOMotorClient(connection_string, tls=True, tlsAllowInvalidCertificates=True)

database = client.Website
admin_collection = database.Admin

# Find an admin by ID
async def fetch_one_admin(id):
    document = await admin_collection.find_one({"_id": id})
    return document

# Get all the admins
async def fetch_all_admins():
    admins = await admin_collection.find().to_list(1000) #1000 is just a random number, since to_list needs an argument which is the length
    print("admins: ",admins)

    return admins

async def register_admin(admin):
    document = admin
    result = await admin_collection.insert_one(document)
    return document

#update document should be implemented
# async def update_admin(id, admin):
   #  await admin_collection.update_one({"id": id}, )

