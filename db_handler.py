from pymongo import MongoClient

# Create env.py file to set connection, db and collection name from mongoDB
from env import CONNECTION_LINK, DB_NAME, COLLECTION_NAME


class Database:

    # Constructor...
    def __init__(self):

        # Connecting to mongoDB...
        cluster = MongoClient(CONNECTION_LINK)
        db = cluster[DB_NAME]

        # Getting instance of collection...
        self.collection = db[COLLECTION_NAME]


