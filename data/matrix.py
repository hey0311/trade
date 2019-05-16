import requests
import datetime
import time
import json

import pandas as pd

# token = 'A8Sk0Rfz' #15600760037 hey7520 用完
# token = 'Hk5jfyt5' #hey0311@qq.com yarnstart123 用完
# token = 'XIXADQ0D' #hey0311@foxmail.com webpack123 用完
# token = 'jr5WbEOp' #13641294686 hey7520 用完
token = 'u2fPK9yR'  # 409620155@qq.com react123
# token = 'ajHewWnR' hey0311@126.com redux123
# token = '8ELP2rPy' lvren1969@gmail.com angular123
headers = {"Authorization": token, "Content-type": "application/json"}
symbol = 'ETC'
interval = '1d'

# startDate=datetime.datetime(2018, 8, 23, 0, 0, 0, 0)
startDate = datetime.datetime(2014, 8, 6, 0, 0, 0, 0)
# startDate = datetime.datetime(2019, 5, 13, 16, 0, 0, 0)
endDate = startDate + datetime.timedelta(days=480)
stopDate = datetime.datetime(2019, 5, 15, 23, 0, 0, 946118)

while startDate < stopDate:
    requireStr = "https://api.matrixdata.io/matrixdata/api/v1/barchart?symbol=" + symbol + "/USD.OK.Q&interval=" + interval + "&start=" + startDate.strftime(
        "%Y-%m-%d %H:%S:%M") + "&end=" + endDate.strftime("%Y-%m-%d %H:%S:%M") + "&limit=500"
    print(requireStr)
    response = requests.get(requireStr, headers=headers)
    data = response.json()

    if data['Head']['Code'] == '200':
        df = pd.DataFrame.from_records(data['Result'])
        filename = symbol + interval + '/' + startDate.strftime("%Y-%m-%d") + '_' + (endDate-datetime.timedelta(days=1)).strftime(
            "%Y-%m-%d") + '.csv'
        print('请求成功!生成' + filename)
        df.to_csv(filename, index=False)
        startDate = startDate + datetime.timedelta(days=480)
        endDate = endDate + datetime.timedelta(days=480)
        if stopDate < endDate:
            endDate = stopDate
        # time.sleep(50)
    else:
        print('请求失败!')
print('程序已结束')
