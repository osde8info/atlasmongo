
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

# # Print all environment variables
# for key, value in os.environ.items():
#     print(f"{key}: {value}")

dbuser=os.environ.get('DBUSER')
dbpass=os.environ.get('DBPASS')
dburl=os.environ.get('DBURL')

uri= f"mongodb+srv://{dbuser}:{dbpass}@{dburl}"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
