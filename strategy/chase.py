import numpy as np
import pandas as pd
from util.myplot import plot_minute_kline


df = pd.DataFrame(np.load('../data/eth1210-0114.npy'),
                  columns=['time', 'open', 'high', 'low', 'close', 'volume', '5minRate'])
df['date']=df['time']
df = df.set_index('date')
df=df[df['time'].notnull()]
# 如果5分钟上涨幅度>1，拿出10%买多，并继续上涨1%后卖出获利。下跌5%爆仓出局
# 成交价不确定,有手续费,看特殊时期,没有全市场回测,最佳参数?,极端情况,网络延迟
account = 100
order_buy = {
    'price': 0,
    'amount': 0
}
hasOrderBuy = False
order_sell = {
    'price': 0,
    'amount': 0
}
hasOrderSell = False
marginLevel=10
stopWin=2
stopLost=1
plot={
    'start':0,
    'end':0
}
for row_index, row in df.iterrows():
    if row['5minRate'] >= 1:
        if hasOrderBuy:
            rate = (row['close'] - order_buy['price']) / order_buy['price'] * 100
            if rate <= -1*stopLost:
                hasOrderBuy = False
                account = account + order_buy['amount'] * (1 + rate * marginLevel/100)
                # print('出局',row['close'])
                if plot['end'] ==0:
                    plot['end']=row_index
            if rate >= stopWin:
                account = account + order_buy['amount'] * (1 + rate * marginLevel/100)
                hasOrderBuy = False
                # print('获利',row['close'])
                if plot['end'] ==0:
                    plot['end']=row_index
        else:
            order_buy['price'] = row['close']
            order_buy['amount'] = account * 0.1
            account -= account * 0.1
            hasOrderBuy = True
            # print('下单买多:',order_buy['price'])
            if plot['start']==0:
                plot['start']=row_index
    if row['5minRate'] <= -1:
        if hasOrderSell:
            rate = (row['close'] - order_sell['price']) / order_sell['price'] * 100
            if rate >= stopLost:
                hasOrderSell = False
                account = account + order_sell['amount'] * (1 + rate * marginLevel/100)
                # print('出局',row['close'])
            if rate <= -1*stopWin:
                account = account + order_sell['amount'] * (1 + rate * marginLevel/100)
                hasOrderSell = False
                # print('获利',row['close'])
        else:
            order_sell['price'] = row['close']
            order_sell['amount'] = account * 0.1
            account -= account * 0.1
            hasOrderSell = True
            # print('下单卖空:',order_sell['price'])
if hasOrderBuy:
    account+=order_buy['amount']
if hasOrderSell:
    account+=order_sell['amount']
df_1 = df[['time','open',  'high', 'low','close']]
# print(plot['start'],plot['end'])
plot_minute_kline(df_1.loc[plot['start']:plot['end']])
print(account)
