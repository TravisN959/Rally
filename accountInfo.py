import pymongo

client = pymongo.MongoClient("mongodb+srv://Travis:Rally@accounts.gqj8e.mongodb.net/Rally?retryWrites=true&w=majority")
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