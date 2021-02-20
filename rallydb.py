import pymongo
import mongoKEYS
client = pymongo.MongoClient(mongoKEYS.getKEY())
# from boto.s3.connection import S3Connection
# client = S3Connection(os.environ['MONGO_KEY'])
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