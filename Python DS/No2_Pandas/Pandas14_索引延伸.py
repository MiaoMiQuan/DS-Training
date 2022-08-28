# Mmq's Data Science Training
# Created at: 2022/8/28 15:26
import pandas as pd
import numpy as np
data=pd.DataFrame(np.arange(10).reshape(5,2),index=np.arange(5)[::-1],columns=['A','B'])
print(data)
print(data.isin([2,3,4]))
print(data[data>2])
print(data.where(data==2,1)) #满足条件的原封不动，不满足条件的改为另一个值
print(data.query('(A<B) & (A<3)')) #返回满足条件的行