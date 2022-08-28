import pandas as pd
import numpy as np
import datetime
#datetime方法
d1=datetime.datetime(year=2022,month=8,day=26,hour=15,minute=30,second=10)
print(d1)

#时间戳方法
d2=pd.Timestamp('2022-8-26')
print(d2)
print(d2.year,d2.month,d2.year)
print(d2+pd.Timedelta('10 days'))

#to_datetime方法
print(pd.to_datetime('2022-8-26'))
print(pd.to_datetime('8/26/2022'))
print(pd.to_datetime('26/8/2022'))

#series边datetime
to_trans=pd.Series(['2022-8-23','2022-08-24','2022-08-25'])
after_trans=pd.to_datetime(to_trans)
print(after_trans)
print(after_trans.dt.hour,after_trans.dt.weekday) #变series后查看性质

#date_range构造时间范围
rg=pd.Series(pd.date_range(start='2022-08-21',end='2022-09-25',freq='2 D'))
print(rg)

#时间当索引后，特殊功能
data=pd.DataFrame(index=pd.date_range(start='2022-01-01',end='2022-02-28',freq='1D'),columns=['A','B'],
                  data=np.array([x for x in range(118)]).reshape(59,2))
print(data)
print(data.loc['2022-01']) #对索引可以这么用
print(data[data.index.month==1]) #对非索引也可以用相同效果
# print(data.between_time('8:00','10:00')) #用来筛选每天里的时间范围

# data=pd.Series(pd.date_range(start='2022-01-01',end='2022-02-05',freq='1D'))
# print(data)

#时间序列重采样
re_data=data.resample('M').sum()
print(re_data)
