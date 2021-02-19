import pymongo

import mongoKEYS
client = pymongo.MongoClient(mongoKEYS.getKEY())
database = client["Rally"]
collection = database["AccountLogin"]

def checkDuplicateUsername(username):
    query = {
        "username" : username
    }
    found = collection.count_documents(query, limit = 1)

    if found != 0:
        return True
    else:
        return False

def addAccount(username, password):
    info = {
        'username' : username,
        'password' : password
    }
    collection.insert_one(info)
    return True

def validateLogin(username, password):
    query = {
        "username": username,
        "password": password
    }
    found = collection.count_documents(query, limit = 1)
    if found != 0:
        return True
    else:
        return False
