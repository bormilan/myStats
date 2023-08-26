from pymongo import MongoClient
from ms_config import CONNECTION_STRING 

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['myBet']

db = get_database()