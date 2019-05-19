import pymongo
from datetime import datetime
import arrow
from util.myplot import plot_minute_kline
import pandas as pd
client=pymongo.MongoClient(host='localhost',port=27017)
db=client.okex
co=db.BTC_Q_1M
start=arrow.get(datetime(2019,5,19,0,0,0,0)).timestamp*1000
end=arrow.get(datetime(2019,5,19,8,0,0,0)).timestamp*1000
print(start,end)
result=co.find({'_id':{'$gte':start,'$lte':end}})
# result=co.find({})
# for item in result:
#     print(item)
r=pd.DataFrame(list(result))
plot_minute_kline(r)