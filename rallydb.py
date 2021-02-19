import pymongo
import mongoKEYS
client = pymongo.MongoClient(mongoKEYS.getKEY())
database = client["Rally"]
collection = database["Rallys"]

def setupRally(idNum, name, description, address, imageAddress, link, eventDate, topic, creator):
    rally = {
        "idNum": idNum,
        "name" : name,
        "description": description,
        "address": address,
        "imageAddress": imageAddress,
        "link": link,
        "eventDate": eventDate,
        "topic": topic,
        "creator": creator
    }
    collection.insert_one(rally)

def getRallys():
    return collection.find({})

def getRallyCount():
    return collection.count_documents({})