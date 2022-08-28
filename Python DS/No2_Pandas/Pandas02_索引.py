import pandas as pd
df=pd.read_csv('titanic.csv')
# 选择指定几列
# a=df['Age']
# a=df[['Age','Name']]
# b=df.iloc[:,3]
# b=df.iloc[:,[2,4,6]]
# c=df.loc[:,'Name']
# c=df.loc[:,['Name','Fare']]
# print(a)
# print(b)
# print(c)

# 选择指定几行
# a=df.iloc[:,2]
# a=df.iloc[:,[2,4,6]]
# b=df.loc[0]
# b=df.loc[[0,3]]
# c=df.set_index('Name')
# d=c.loc['Heikkinen, Miss. Laina']
# d=c.loc[['Heikkinen, Miss. Laina','Futrelle, Mrs. Jacques Heath (Lily May Peel)']]
# print(a,'\n-------------')
# print(b,'\n-------------')
# print(d,'\n-------------')

# 选择行列
# a=df.iloc[1:2,3:4]
# b=df.loc[0:3,['Fare','Name']]
# c=df.set_index('Name')
# d=c.loc[['Heikkinen, Miss. Laina','Futrelle, Mrs. Jacques Heath (Lily May Peel)'],['Fare','Survived']]
# e=c.loc['Heikkinen, Miss. Laina':'Moran, Mr. James']
# print(a)
# print(b)
# print(d)
# print(e)

# 数值修改
# df.loc[0,'Fare']=10000
# print(df.head())