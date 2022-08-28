import pandas as pd
import numpy as np
df=pd.DataFrame({'key':['a','b','c','d','a','b','c','a','b','a'],
                'data':[x for x in range(10)]})
# print(df)

# 非groupby方法
# for key in ['a','b','c']:
#     print(key,df[df['key']==key].sum())
# print(df['key'])
# print(df.loc[:,'key'])

# groupby 方法
# a=df.groupby('key').sum()
# print(a)
# b=df.groupby('key').aggregate(np.sum)
# print(b)

df=pd.read_csv('titanic.csv')
print(df.groupby('Sex').head(3),'对sex的每类只取前head个')
print(df.groupby('Sex')['Age'].mean())
print(df.groupby('Sex')['Survived'].mean())
