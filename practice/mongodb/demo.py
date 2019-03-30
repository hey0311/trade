import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students
student1 = {
    'id': '20170103',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

result = collection.insert_many([student1, student2])

print(result)