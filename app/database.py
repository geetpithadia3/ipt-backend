import pymongo
from bson.json_util import dumps


class DB(object):
    URI = 'mongodb+srv://geet:admin@progresstracker-ocrea.gcp.mongodb.net/test?retryWrites=true&w=majority'

    """ Database related operations defined here"""
    @staticmethod
    def init():
        client = pymongo.MongoClient(DB.URI)
        DB.DATABASE = client.progress_tracker

    @staticmethod
    def insert(collection, data):
        DB.DATABASE[collection].insert(data)

    @staticmethod
    def find_one(collection, query):
        return DB.DATABASE[collection].find_one(query)

    @staticmethod
    def find(collection):
        return dumps(DB.DATABASE[collection].find())

