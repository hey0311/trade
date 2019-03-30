import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from util.myplot import plot_minute_kline
from util.Order import Order
from util.Account import Account
import mpl_finance as mpf

df = pd.DataFrame(np.load('../data/eth1210-0114_day.npy'),
                  columns=['time', 'open', 'high', 'low', 'close', 'volume', '5minRate'])
df['time']=pd.to_datetime(df['time'],format="%Y-%M-%D")
df = df.set_index('time')
df = df[df.index.notnull()]
print(df.head())
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
# 设置X轴刻度为日期时间
ax.xaxis_date()
plt.xticks(rotation=45)
plt.yticks()
plt.title("股票代码：601558两年K线图")
plt.xlabel("时间")
plt.ylabel("股价（元）")
# 注意数据格式
mpf.candlestick_ohlc(ax,df.index.values.append(df.values[:,0:-1]),width=1.5,colorup='r',colordown='green')
plt.show()