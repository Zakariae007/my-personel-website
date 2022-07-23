import os
from dotenv import load_dotenv
import motor.motor_asyncio 

load_dotenv()

def connect_db(): 
    connection_string = os.getenv('DB_URL')

    client = motor.motor_asyncio.AsyncIOMotorClient(connection_string, tls=True, tlsAllowInvalidCertificates=True)

    database = client.Website
    return database

