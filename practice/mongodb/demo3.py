import pymongo
client=pymongo.MongoClient(host='localhost',port=27017)
db=client.okex
co=db.etc3
import datetime
start=datetime.datetime(2019,4,3,5)
end=datetime.datetime(2019,4,3,15)
result=co.find({'date':{'$gt':start,'$lt':end}})
from util import utils
data=utils.tran_mongo_2_df(result)
print(data)
from util.myplot import  plot_minute_kline
plot_minute_kline(data.iloc[:,0:5])

