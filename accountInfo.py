import pymongo

import mongoKEYS
client = pymongo.MongoClient(mongoKEYS.getKEY())
database = client["Rally"]
collection = database["AccountInfo"]

def setupAccount(username, phone, email, topics, fname, lname, address):
    acct = {
        "username" : username,
        "phone": phone,
        "email": email,
        "topics": topics,
        "fname": fname,
        "lname": lname,
        "address": address
    }
    collection.insert_one(acct)

def getInfo(username):
    return collection.find_one({"username": username})

def getAddress(username):
    address = collection.find_one({"username": username})["address"]
    return address["street"] + ', ' + address["city"] + ", " + address["state"] + " " + address["zip"]

def setTopics(username, newTopics):
    collection.update_one({"username": username}, {"$set":{"topics": newTopics}})

def getTopics(username):
    info = getInfo(username)
    return info["topics"]

def getAccounts():
    return collection.find({})