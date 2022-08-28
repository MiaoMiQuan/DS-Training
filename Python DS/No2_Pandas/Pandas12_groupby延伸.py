# Mmq's Data Science Training
# Created at: 2022/8/28 11:15
import pandas as pd
import numpy as np
data=pd.read_csv('titanic.csv')

# grouped=data.groupby(['Sex','Survived'])
# print(grouped.count())

#归类groupby
# def age_label(age):
#     if age<18:
#         return 'under 18'
#     else:
#         return 'beyond 18'
#
# grouped=data.groupby(age_label)
# print(grouped.count())

#展示groupby后组内数据
# grouped=data.groupby(['Sex','Survived'])
# print(grouped.first()) #展示每组值的第一个
# print(grouped.last()) #展示每组值的最后一个

#只关注groupby后的一部分,把多余数据删掉
# wanted_data=data.groupby(['Sex','Survived']).get_group(('female',0))
# print(wanted_data)

#多重索引
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
index=pd.MultiIndex.from_arrays(arrays=arrays,names=['first','second'])
s=pd.DataFrame(np.random.randn(8,2),index=index)
print(s)
# print(s.groupby(level=0).sum())
# print(s.groupby(level=1).sum())
# print(s.groupby(['first']).aggregate(np.sum))

#as_index,标识groupby后的特征是否作为一个column
df = pd.DataFrame(data={'books':['bk1','bk1','bk1','bk2','bk2','bk3'], 'price': [12,12,12,15,15,17]})
print(df)
print(df.groupby('books', as_index=True).sum())
print(df.groupby('books', as_index=False).sum())
print(df.groupby('books').sum().reset_index()) #reset_index重新构建索引


