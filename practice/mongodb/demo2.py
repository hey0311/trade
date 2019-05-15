import pymongo
from datetime import datetime
client=pymongo.MongoClient(host='localhost',port=27017)
db=client.okex
co=db.etc3
start=datetime(2019,4,2,22)
end=datetime(2019,4,2,23)
result=co.find({'date':{'$gte':start,'$lte':end}})
for item in result:
    print(item)