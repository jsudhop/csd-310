#Jon Sudhop
#11-14-21

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.yjyss.mongodb.net/pytech"
client = MongoClient(url, tlsAllowInvalidCertificates=True)
db = client.pytech

info = db.students.find({})

print("--Displaying Students Documents From find() Query--")
for each in info:
    print(f'\n Student ID: {each["student_id"]}\nFirst Name: {each["first_name"]}\nLast Name: {each["last_name"]}')

print("--Displaying Student Document From find_one() Query--")
doc = db.students.find_one({"student_id": "1007"})
print(f'\nStudent ID: {doc["student_id"]}\nFirst Name: {doc["first_name"]}\nLast Name: {doc["last_name"]}')