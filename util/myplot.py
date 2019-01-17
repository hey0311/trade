import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import mpl_finance as mpf
from matplotlib.ticker import Formatter
import numpy as np
def plot_minute_kline(dfcvs):
    dfcvs.columns = ['时间','开盘','最高','最低','收盘']
    dfcvs['时间']=pd.to_datetime(dfcvs['时间'],format="%Y/%m/%d-%H:%M")
    #matplotlib的date2num将日期转换为浮点数，整数部分区分日期，小数区分小时和分钟
    #因为小数太小了，需要将小时和分钟变成整数，需要乘以24（小时）×60（分钟）=1440，这样小时和分钟也能成为整数
    #这样就可以一分钟就占一个位置
    dfcvs['时间']=dfcvs['时间'].apply(lambda x:dates.date2num(x)*1440)
    data_mat=dfcvs.values

    fig,ax=plt.subplots(figsize=(15,5))

    fig.subplots_adjust(bottom=0.1)
    mpf.candlestick_ohlc(ax,data_mat,colordown='r', colorup='g',width=0.5,alpha=1)
    #将x轴的浮点数格式化成日期小时分钟
    #默认的x轴格式化是日期被dates.date2num之后的浮点数，因为在上面乘以了1440，所以默认是错误的
    #只能自己将浮点数格式化为日期时间分钟
    #参考https://matplotlib.org/examples/pylab_examples/date_index_formatter.html
    class MyFormatter(Formatter):
        def __init__(self, dates, fmt='%m-%d %H:%M'):
            self.dates = dates
            self.fmt = fmt
        def __call__(self, x, pos=0):
            'Return the label for time x at position pos'
            ind = int(np.round(x))
            #ind就是x轴的刻度数值，不是日期的下标

            return dates.num2date( ind/1440).strftime(self.fmt)

    formatter = MyFormatter(data_mat[:,0])
    ax.xaxis.set_major_formatter(formatter)

    for label in ax.get_xticklabels():
        label.set_rotation(30)
        label.set_horizontalalignment('right')
    # plt.text(dfcvs['时间'][30], dfcvs['最高'][30], 'buy')
    plt.show()