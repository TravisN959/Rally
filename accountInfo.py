import pymongo

client = pymongo.MongoClient("mongodb+srv://Travis:Rally@accounts.gqj8e.mongodb.net/Rally?retryWrites=true&w=majority")
database = client["Rally"]
collection = database["AccountInfo"]