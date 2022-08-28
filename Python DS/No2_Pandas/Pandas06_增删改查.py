import pandas as pd
# 创建series
data=['1','2','3']
index=['a','b','c']
df=pd.Series(data=data,index=index)

# 查找
# print(df)
# print(df[0])
# print(df.iloc[0],df.loc['a'])
# print(df[[True,False,True]])

# 修改数值(改一个)
# b=df.copy()
# b[0]=10
# print(b)
# b.replace(to_replace=10,value=100,inplace=True)
# print(b)

# 修改index（改一堆+改一个）
# b=df.copy()
# print(b.index)
# b.index=['a','b','d']
# print(b)
# b.rename(index={'a':'A'},inplace=True)
# print(b)

# 增加
# a=df.copy()
# b=df.copy()
# c=pd.concat([a,b])
# print(c)
# c['e']=100
# print(c)
# c=pd.concat([a,b],ignore_index=True)
# print(c)
# c=pd.concat([a,b],axis=1)
# print(c)
# c.loc['e']=[4,4]
# print(c)

# Series删除一个
# print(df)
# del df['a']
# print(df)

# Series删除多个
# print(df)
# df.drop(['a','b'],inplace=True)
# print(df)

# df增加
# df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['A','B','C'])
# print(df)
# df.loc[3]=[10,11,12]
# print(df)
# df['D']=[3,6,9,12]
# print(df)

# df删
# df=pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],columns=['A','B','C','D'],index=['a','b','c','d'])
# print(df)
# df.drop(['a','b'],axis=0,inplace=True)
# print(df)
# df.drop(['A','B'],axis=1,inplace=True)
# print(df)
df=pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],columns=['A','B','C','D'],index=['a','b','c','d'])
del df[['A','B']]
print(df)