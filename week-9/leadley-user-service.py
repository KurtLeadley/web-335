## Title: leadley-user-service.py
## Author: Kurt Leadley, Professor Krasso
## Date: 12/10/2019
## Description: Python Script to add new user to mongo (if the email is unique)

## import dependencies (step 3)
import pprint
import datetime
import pymongo
## connect to our local mongoDB (step 4)
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.web335
## create a new user document (step 5)
user = {
    "first_name": "Pie",
    "last_name": "Thawn",
    "employee_id": "7777777",
    "email": "python@me.com",
    "date_created": datetime.datetime.utcnow()
}
## user.email wasn't working, just repeat email here for checking later
email = "python@me.com"
## if the email does not already exist in the system, insert the user document
if db.users.count_documents({"email" : email}, limit = 1) == 0:
    ## get this users auto generated id and also insert the user document into mongo (step 6)
    user_id = db.users.insert_one(user).inserted_id
    ## print out the automatically generated id, note the type cast to string (step 7)
    print("")
    print("Auto Generated ID: " + str(user_id))
    print("")
## if the email already exists, find the user details by email
else:
    existing_user = db.users.find_one({"email":email})
    ## get this users auto generated id
    user_id = existing_user.get("_id")
    ## print out the automatically generated id, note the type cast to string (step 7)
    print("")
    print("Auto Generated ID: " + str(user_id))
    print("")
## pretty print the entire user document by _id (step 8 & 9)
print("User Details:")
pprint.pprint(db.users.find_one({"_id": user_id}))