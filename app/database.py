# DB class
# Operations dealing with the database are mentioned in this file
import pymongo
from bson.json_util import dumps


class DB(object):
    URI = 'mongodb+srv://geet:admin@progresstracker-ocrea.gcp.mongodb.net/test?retryWrites=true&w=majority'

    @staticmethod
    def init():
        client = pymongo.MongoClient(DB.URI)
        DB.DATABASE = client.progress_tracker

    @staticmethod
    def insert(collection, data):
        DB.DATABASE[collection].insert(data)

    @staticmethod
    def update(collection, criteria, query):
        DB.DATABASE[collection].update(criteria,{'$set':query})
       
    @staticmethod
    def find_one(collection, query):
        return DB.DATABASE[collection].find_one(query)

    @staticmethod
    def find(collection, query={}, projection={}):
        if(projection=={}):
            return DB.DATABASE[collection].find(query)
        else:
            return DB.DATABASE[collection].find(query,projection)


    @staticmethod
    def count(collection,query):
        return DB.DATABASE[collection].find(query).count()

