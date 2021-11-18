#jon sudhop
#11-18-21

from pymongo import MongoClient
#connecting
url = "mongodb+srv://admin:admin@cluster0.yjyss.mongodb.net/pytech"
client = MongoClient(url, tlsAllowInvalidCertificates=True)
db=client.pytech

info = db.students.find({})

#initial print
print("--Displaying Students Documents From find() Query--")
for each in info:
    print(f'Student ID: {each["student_id"]}\nFirst Name: {each["first_name"]}\nLast Name: {each["last_name"]}\n')

#change
filter = {'student_id': '1007'}
newName = {'$set': {'last_name': 'FromDaBlock'}}

db.students.update_one(filter, newName)

#final reprint
print("--Displaying Student Document From find_one() Query--")
doc = db.students.find_one({"student_id": "1007"})
print(f'Student ID: {doc["student_id"]}\nFirst Name: {doc["first_name"]}\nLast Name: {doc["last_name"]}\n')