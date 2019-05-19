# 存到mongodb数据库
import pymongo
import json
import numpy as np
from dateutil import parser
import datetime
import pandas as pd
import time
from collections import OrderedDict
import csv
import arrow
from util import utils

pd.set_option('display.max_rows', 50)  # 最大行数
pd.set_option('display.max_columns', 50)  # 最大列数
pd.set_option('display.width', 4000)  # 页面宽度
dir = 'okex/BTC/1m_Q'
files = utils.reverseDir(dir)
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.okex
collection = db.BTC_Q_1M
for file in files:
    file_path = dir + '/' + file
    # 读取csv至字典
    csvFile = open(file_path, "r")
    reader = csv.reader(csvFile)
    result = {}
    for item in reader:
        # 忽略第一行
        if reader.line_num == 1:
            continue
        result[item[7]] = item
    csvFile.close()
    # 将list转换到dataframe
    r = pd.DataFrame(result,
                     index=['close', 'high', 'low', 'open', 'quoteVolume', 'volume', 'symbol', 'time', 'tradeNum'])
    r = r.T
    r['_id'] = r['time'].apply(lambda x: parser.parse(x))
    print('处理'+file)
    # 插入mongodb
    try:
        result = collection.insert_many(json.loads(r.T.to_json()).values(),ordered=False)
    except:
        print('error')
