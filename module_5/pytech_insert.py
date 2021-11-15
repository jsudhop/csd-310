#Jon Sudhop
#11-14-21

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.yjyss.mongodb.net/pytech"
client = MongoClient(url, tlsAllowInvalidCertificates=True)
db=client.pytech

jenny = {
    "student_id": "1007",
    "first_name": "Jenny",
    "last_name": "Jenny",
    "Enrollment": [
        {
            "term": "01",
            "gpa": "4.0",
            "start_date": "10-21-2015",
            "end_date": "01-23-2016",
            "Courses": [
                {
                    "course_id": "113",
                    "description": "Pottery",
                    "instructor": "Patrick S.",
                    "grade": "A"
                },
                {
                    "course_id": "208",
                    "description": "Relativistic Physics",
                    "instructor": "Albert E.",
                    "grade": "A"
                },
                {
                    "course_id": "306",
                    "description": "Anatomy and Physiology",
                    "instructor": "Jack T. R.",
                    "grade": "A"
                }
            ]
        }
    ]
}

francis = {
    "student_id": "1008",
    "first_name": "Francis",
    "last_name": "Coppola",
    "Enrollment": [
        {
            "term": "01",
            "gpa": "4.0",
            "start_date": "01-30-2016",
            "end_date": "04-20-2016",
            "Courses": [
                {
                    "course_id": "402",
                    "description": "English Literature",
                    "instructor": "John R. R. T.",
                    "grade": "A"
                },
                {
                    "course_id": "210",
                    "description": "Cosmology",
                    "instructor": "Stephen H.",
                    "grade": "A"
                },
                {
                    "course_id": "503",
                    "description": "Archeology",
                    "instructor": "Henry J. jr",
                    "grade": "A"
                }
            ]
        }
    ]
}

steve = {
    "student_id": "1009",
    "first_name": "Steve",
    "last_name": "McDonald",
    "Enrollment": [
        {
            "term": "01",
            "gpa": "4.0",
            "start_date": "01-30-2016",
            "end_date": "04-20-2016",
            "Courses": [
                {
                    "course_id": "402",
                    "description": "English Literature",
                    "instructor": "John R. R. T.",
                    "grade": "A"
                },
                {
                    "course_id": "208",
                    "description": "Relativistic Physics",
                    "instructor": "Albert E.",
                    "grade": "A"
                },
                {
                    "course_id": "503",
                    "description": "Archeology",
                    "instructor": "Henry J. jr",
                    "grade": "A"
                },
                {
                    "course_id": "306",
                    "description": "Anatomy and Physiology",
                    "instructor": "Jack T. R.",
                    "grade": "A"
                }
            ]
        }
    ]
}

jenny_student_id = db.students.insert_one(jenny).inserted_id
print("Inserted student record Jenny Jenny into the students collection with document id ", jenny_student_id)
francis_student_id = db.students.insert_one(francis).inserted_id
print("Inserted student record Francis Coppola into the students collection with document id ", francis_student_id)
steve_student_id = db.students.insert_one(steve).inserted_id
print("Inserted student record Steve McDonald into the students collection with document id ", steve_student_id)