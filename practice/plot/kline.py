from util.myplot import plot_minute_kline
import pandas as pd
import numpy as np
df = pd.DataFrame(np.load('../../data/eth1210-0114.npy'),
                  columns=['time', 'open', 'high', 'low', 'close', 'volume','rate'])
# df = df.set_index('time')
# df['time'].fillna(df['time'][0])
# df.dropna()
# df.drop(df['time'].isnull())
df=df[df['time'].notnull()]

# df['timestamp'] = df['time'].apply(lambda x:time.mktime(x.timetuple()))
df = df[['time','open',  'high', 'low','close']]
print(df.head())
dfcvs=df.iloc[:100,:]

plot_minute_kline(dfcvs)