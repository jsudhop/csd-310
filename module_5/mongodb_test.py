from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.yjyss.mongodb.net/pytech"
client = MongoClient(url, tlsAllowInvalidCertificates=True)
db=client.pytech
print(db.list_collection_names())
