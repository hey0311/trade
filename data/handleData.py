import numpy as np
import pandas as pd
from collections import OrderedDict
import json

result = np.loadtxt("raw/ltc.csv")
dfIndex = ['ticker' + str(i) for i in range(result.shape[0])]
columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
df = pd.DataFrame(result, index=dfIndex, columns=columns)
df['time'] = pd.to_datetime(df['timestamp'], unit='ms')+ pd.Timedelta('08:00:00')
df['date'] = pd.to_datetime(df['timestamp'], unit='ms')+ pd.Timedelta('08:00:00')
df['date'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
df = df.set_index('time')
# df.resample('1D').holc()
# print(df.head())
# df=df.drop(columns='timestamp',axis=1)
df = df.resample('1T').agg(
    OrderedDict([
        ('open', 'first'),
        ('high', 'max'),
        ('low', 'min'),
        ('close', 'last'),
        ('volume', 'sum'),
        ('date','first')
    ])
)
df = df[['date','open', 'high', 'low', 'close', 'volume']]
df['rate']=df['close'].pct_change(5)*100

print(df)
# np.save("ltc.npy", df)

#存到mongodb数据库
import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.ltc

result = collection.insert_many(json.loads(df.T.to_json()).values())

print(result)