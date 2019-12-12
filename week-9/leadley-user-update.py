## Title: leadley-user-update.py
## Author: Kurt Leadley, Professor Krasso
## Date: 12/12/2019
## Description: Python Script to update a document

## import dependencies 
import pprint
import datetime
import pymongo
## connect to our local mongoDB
from pymongo import MongoClient
client = MongoClient("localhost", 27017)
db = client.web335

## use the update_one method to update Pie Thawn's email address
db.users.update_one(
    {"employee_id" : "7777777"},
    {
        "$set" :{
            "email":"kleadley@my365.bellevue.edu"
        }
    }
)
## query the database and select the fields to print by using 
## the second argument of find_one (set to 1)
pprint.pprint(db.users.find_one
    (
        {"employee_id" : "7777777"},
        {"email":1, "employee_id":1,"first_name":1,"last_name":1}
    )
)