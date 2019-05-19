import requests
import datetime
import time
import json
import os

import pymongo
from dateutil import parser
import pandas as pd
from util import utils
pd.set_option('display.max_rows', 50)  # 最大行数
pd.set_option('display.max_columns', 50)  # 最大列数
pd.set_option('display.width', 4000)  # 页面宽度

# token = 'A8Sk0Rfz' #15600760037 hey7520 用完
# token = 'Hk5jfyt5' #hey0311@qq.com yarnstart123 用完
# token = 'XIXADQ0D' #hey0311@foxmail.com webpack123 用完
# token = 'jr5WbEOp' #13641294686 hey7520 用完
# token = 'u2fPK9yR'  # 409620155@qq.com react123 用完
# token = 'ajHewWnR' #hey0311@126.com redux123 用完
token = '8ELP2rPy'  # lvren1969@gmail.com angular123
headers = {"Authorization": token, "Content-type": "application/json"}
symbol = 'BTC'
symbol_suffix = '/USD.OK.'
symbol_type='Q'
interval = '1m'
#开始时间
year = 2019
month = 5
day = 13
hour = 16

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.okex
collection = db.BTC_Q_1M
startDate = datetime.datetime(year, month, day, hour, 0, 0, 0)
if interval == '1m':
    timedelta = datetime.timedelta(hours=8)
elif interval == '1d':
    timedelta = datetime.timedelta(days=480)

endDate = startDate + timedelta
now = datetime.datetime.now()

while startDate < now:

    dir_path='okex/' + symbol + '/' + interval+'_'+symbol_type+'/'
    utils.mkdir(dir_path)
    filename = startDate.strftime("%Y-%m-%d(%H") + '-' + \
               endDate.strftime("%H)") + '.csv'
    if os.path.exists(dir_path+filename):
        print(filename+'已存在,跳过')
    else:
        requireStr = "https://api.matrixdata.io/matrixdata/api/v1/barchart?symbol=" + \
                    symbol + symbol_suffix+symbol_type+\
                    "&interval=" + interval + \
                    "&start=" + startDate.strftime("%Y-%m-%d %H:%S:%M") + \
                    "&end=" + endDate.strftime("%Y-%m-%d %H:%S:%M") + \
                    "&limit=500"
        print(requireStr)
        response = requests.get(requireStr, headers=headers)
        data = response.json()
        if data['Head']['Code'] == '200':
            df = pd.DataFrame.from_records(data['Result'])
            df.to_csv(dir_path+filename, index=False)
            df.columns=['close', 'high', 'low', 'open', 'quoteVolume', 'volume', 'symbol', 'time', 'tradeNum']
            df['_id'] = df['time'].apply(lambda x: parser.parse(x))
            # 插入mongodb

            try:
                result = collection.insert_many(json.loads(df.T.to_json()).values(),ordered=False)
            except:
                pass
        else:
            print('请求失败!')
    startDate = startDate + timedelta
    endDate = endDate + timedelta
    if now < endDate:
        endDate = now
    time.sleep(1)
print('程序已结束')
