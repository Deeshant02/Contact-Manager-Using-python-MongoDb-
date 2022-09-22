import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["contact_manager"]
collection = db["contact_no"]

name = "mokal"

if(collection.find_one({"first_name": name}) != None):
    lst = (collection.find({"first_name": name}))
else:
    lst = (collection.find({"last_name": name}))

print(lst)