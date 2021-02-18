import pymongo

client = pymongo.MongoClient("mongodb+srv://Travis:Rally@accounts.gqj8e.mongodb.net/Rally?retryWrites=true&w=majority")
database = client["Rally"]
collection = database["AccountInfo"]

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
