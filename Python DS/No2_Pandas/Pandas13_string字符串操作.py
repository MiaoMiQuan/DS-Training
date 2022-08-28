# Mmq's Data Science Training
# Created at: 2022/8/28 14:48
import pandas as pd
import numpy as np
data=pd.Series(['A_A','b ','C',np.nan])
print(data)
print(data.str.lower())
print(data.str.upper())
print(data.str.len())
print(data.str.strip()) #strip去空格,lstrip去左，rstrip去右
print(data.str.replace('A_A','aaa'))
print(data.str.split('_'))
print(data.str.split('_',expand=True,n=1)) #加更多字段,n为切几次
print(data.str.contains('A'))
print(data.str.get_dummies(sep='_')) #看看里面都有啥元素，元素的排列

