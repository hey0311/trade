import requests
import datetime
import time
import json

import pandas as pd
token = 'A8Sk0Rfz'
fileIndex=0
headers = {"Authorization": token, "Content-type": "application/json"}
symbol='BTC/USD.OK.Q&'
interval='1m'

startDate=datetime.datetime(2018, 8, 23, 0, 0, 0, 0)
endDate=startDate+datetime.timedelta(hours=8)
stopDate=datetime.datetime(2019,5,15,23,0,0,946118)
while stopDate-endDate>datetime.timedelta(hours=1):
    requireStr="https://api.matrixdata.io/matrixdata/api/v1/barchart?symbol="+symbol+"&interval="+interval+"&start="+startDate.strftime("%Y-%m-%d %H:%S:%M")+"&end="+endDate.strftime("%Y-%m-%d %H:%S:%M")+"&limit=500"
    print(requireStr)
    startDate=startDate+datetime.timedelta(hours=8)
    endDate=endDate+datetime.timedelta(hours=8)
    time.sleep(2)
    response=requests.get(requireStr,headers=headers)
    data = response.json()

    if data['Head']['Code'] == '200':
         df = pd.DataFrame.from_records(data['Result'])
         filename='./mdata/'+startDate.strftime("%Y-%m-%d %H:%S:%M")+'.csv'
         print(filename)
         df.to_csv(filename,index = False)