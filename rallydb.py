import pymongo

client = pymongo.MongoClient("mongodb+srv://Travis:Rally@accounts.gqj8e.mongodb.net/Rally?retryWrites=true&w=majority")
database = client["Rally"]
collection = database["Rallys"]

def setupRally(name, description, address, imageAddress, link, eventDate, topic):
    rally = {
        "name" : name,
        "description": description,
        "address": address,
        "imageAddress": imageAddress,
        "link": link,
        "eventDate": eventDate,
        "topic": topic
    }
    collection.insert_one(rally)

def getRallys():
    return collection.find({})