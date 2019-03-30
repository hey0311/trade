import pandas as pd
# df=pd.DataFrame([[1,2,3],[3,4,5]],index=['a','b'],columns=['c1','c2','c3'])
result=pd.to_datetime('1551628800000', unit='ms')+ pd.Timedelta('08:00:00')
print(result)