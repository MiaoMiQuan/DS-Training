import pandas as pd
df=pd.read_csv('titanic.csv')

# 布尔索引锁定行
# a=df['Fare']>40
# print(a)
# print(df[a])
# b=df[df['Age']==20]
# print(b)

# 找特定行
# a=df['Fare']>80
# print(a)
# 特定行的所有列
# b=df.loc[a]
# print(b)
# 特定行的特定列
# c=df.loc[a,'Age']
# print(c)
# d=b.loc[:,'Age']
# print(d)

# 找符合条件的个数
# a=(df['Age']>70).count()
# b=(df['Age']>70).sum() #对布尔求和即为计数
# print(df['Age']>70)
# print(a,b)
# print(df[df['Age']>70]['Age'])
# 符合条件的，对另一列求某种运算
a=df['Age']>70
# b=df.loc[a,'Fare']
b=df[a]['Fare']
print(b)
print(b.sum(),b.mean(),b.count())