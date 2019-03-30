import numpy as np
import pandas as pd

import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.ltc

def foo(arr):
    pass

results = collection.find()
for index,result in results:
    if result['rate'] is not None:
        if result['rate']>1:
            foo(result[index])
            print(result)
