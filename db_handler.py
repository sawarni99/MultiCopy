from pymongo import MongoClient
from constants import MAX_SIZE

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


    # Getting count of datas in db...
    def count(self):
        return self.collection.count({})


    # initializing DB...
    def initialize(self):

        # Checking if DB is empty...
        if self.count() == 0:

            # Interating through max size...
            for index in range(MAX_SIZE):

                # Initializing DB with max size ids...
                self.collection.insert_one({"_id" : index+1})


    # Function to update datas...
    def update(self, texts):

        # Iterating through the texts...
        for index in range(len(texts)):

            # Updating the new values...
            self.collection.update({"_id": index+1}, {"$set":{"text" : texts[index]}})

    
    # Function to get all datas...
    def get_data(self):
        ret = []

        # Getting all the texts...
        results = self.collection.find({})

        for result in results:
            text = None
            # check if text present in databsae...
            if 'text' in result:
                text = result['text']
                ret.append(text)

        return reversed(ret)
