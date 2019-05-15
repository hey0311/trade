import numpy as np
import pandas as pd
from util.myplot import plot_minute_kline
from util.Order import Order
from util.Account import Account

df = pd.DataFrame(np.load('../data/eth1210-0114.npy'),
                  columns=['time', 'open', 'high', 'low', 'close', 'volume', '5minRate'])
df['date'] = df['time']
df = df.set_index('date')
df = df[df['time'].notnull()]
# 如果5分钟上涨幅度>1，拿出10%买多，并继续上涨1%后卖出获利。下跌5%爆仓出局
# 成交价不确定,有手续费,看特殊时期,没有全市场回测,最佳参数?,极端情况,网络延迟
acc = Account()
for row_index, row in df.iterrows():
    if row['5minRate'] >= 1:
        order = Order('buy', row['close'], acc.blance * 0.1, row_index)
        acc.add_order(order)
    acc.deal_order(row['close'],row_index)
df_1 = df[['time', 'open', 'high', 'low', 'close']]
# for p in acc.plots:
#     plot_minute_kline(df_1.loc[p[0]:p[1]])
plot_minute_kline(df_1.loc[acc.plots[0][0]:acc.plots[0][1]])

print(acc.blance)