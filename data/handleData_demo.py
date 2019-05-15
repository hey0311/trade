import numpy as np
data=np.loadtxt('raw/etc0402-0407.csv')
import pandas as pd
data=pd.DataFrame(data,columns=['ts','o','h','l','c','v'])

data['date'] = pd.to_datetime(data['ts'], unit='ms')+ pd.Timedelta('08:00:00')
data['time'] = pd.to_datetime(data['ts'], unit='ms')+ pd.Timedelta('08:00:00')
data = data.set_index('time')
from collections import OrderedDict
data=data.resample('1T').agg(
    OrderedDict([
        ('date','first'),
        ('o','first'),
        ('h','max'),
        ('l','min'),
        ('c','last'),
        ('v','sum')
    ])
)
data=data[['date','o','h','l','c','v']]
import pymongo
client=pymongo.MongoClient(host='localhost',port=27017)
db=client.okex
c=db.etc3
import json
success=c.insert_many(json.loads(data.T.to_json()).values())
print(success)