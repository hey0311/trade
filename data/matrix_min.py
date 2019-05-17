import requests
import datetime
import time
import json

import pandas as pd

# token = 'A8Sk0Rfz' #15600760037 hey7520 用完
# token = 'Hk5jfyt5' #hey0311@qq.com yarnstart123 用完
# token = 'XIXADQ0D' #hey0311@foxmail.com webpack123 用完
# token = 'jr5WbEOp' #13641294686 hey7520 用完
# token = 'u2fPK9yR'  # 409620155@qq.com react123 用完
# token = 'ajHewWnR' #hey0311@126.com redux123 用完
token = '8ELP2rPy'  # lvren1969@gmail.com angular123
headers = {"Authorization": token, "Content-type": "application/json"}
symbol = 'EOS/USD.OK.INDEX'
interval = '1m'
year = 2018
month = 10
day = 16
hour = 0
startDate = datetime.datetime(year, month, day, hour, 0, 0, 0)
if interval == '1m':
    timedelta = datetime.timedelta(hours=8)
elif interval == '1d':
    timedelta = datetime.timedelta(days=480)

endDate = startDate + timedelta
now = datetime.now()

while startDate < now:
    requireStr = "https://api.matrixdata.io/matrixdata/api/v1/indexbarchart?symbol=" + \
                 symbol + \
                 "&interval=" + interval + \
                 "&start=" + startDate.strftime("%Y-%m-%d %H:%S:%M") + \
                 "&end=" + endDate.strftime("%Y-%m-%d %H:%S:%M") + \
                 "&limit=500"
    print(requireStr)
    response = requests.get(requireStr, headers=headers)
    data = response.json()

    if data['Head']['Code'] == '200':
        df = pd.DataFrame.from_records(data['Result'])
        filename = 'matrix_data/' + symbol + '/' + interval + '_index/' + \
                   startDate.strftime("%Y-%m-%d(%H") + '-' + \
                   endDate.strftime("%H)") + '.csv'
        print('请求成功!生成' + filename)
        df.to_csv(filename, index=False)
        startDate = startDate + timedelta
        endDate = endDate + timedelta
        if now < endDate:
            endDate = now
    else:
        print('请求失败!')
print('程序已结束')
