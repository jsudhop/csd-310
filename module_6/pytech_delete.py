#jon sudhop
#11-18-21


#connecting
from bson.objectid import ObjectId
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.yjyss.mongodb.net/pytech"
client = MongoClient(url, tlsAllowInvalidCertificates=True)
db = client.pytech

info = db.students.find({})
id = db.students.find_one({"student_id": "1010"})
final = db.students.find({})

student_Test = {
    "student_id": "1010", 
    "first_name": "Michael", 
    "last_name": "Myers",
    }

#initial print
print("--Displaying Students Documents From find() Query--")
for each in info:
    print(f'Student ID: {each["student_id"]}\nFirst Name: {each["first_name"]}\nLast Name: {each["last_name"]}\n')

#inserting new student
print("--Insert Statements--")
michael_Student_Id = db.students.insert_one(student_Test).inserted_id
print(f'Inserted student record into students collection with document_id', michael_Student_Id)
print('')

#added student print
print("--Displaying Student Test Doc--")
print(f'Student ID: {student_Test["student_id"]}\nFirst Name: {student_Test["first_name"]}\nLast Name: {student_Test["last_name"]}\n')

#deleting test student
db.students.delete_one({"student_id": "1010"})

#final print
print("--Displaying Students Documents From find() Query--")
for each in final:
    print(f'Student ID: {each["student_id"]}\nFirst Name: {each["first_name"]}\nLast Name: {each["last_name"]}\n')
