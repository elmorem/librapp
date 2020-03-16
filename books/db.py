from pymongo import mongo_client

client=MongoClient()

db=client.books

collection = db.book
