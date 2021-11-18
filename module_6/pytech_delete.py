#jon sudhop
#11-18-21

#connecting
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.yjyss.mongodb.net/pytech"
client = MongoClient(url, tlsAllowInvalidCertificates=True)
db=client.pytech

info = db.students.find({})

#initial print
print("--Displaying Students Documents From find() Query--")
for each in info:
    print(f'Student ID: {each["student_id"]}\nFirst Name: {each["first_name"]}\nLast Name: {each["last_name"]}\n')

