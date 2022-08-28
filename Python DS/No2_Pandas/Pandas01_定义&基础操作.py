import pandas as pd
# 数据的读取
df=pd.read_csv('titanic.csv')

# 查看数据基础信息
# print(df.head(5))
# print(df.info())
# print(df.dtypes)
# print(df.index)
# print(df.columns)
# print(df.values)
# print(df.describe())

# 自定义数据集合
# dota_set={'姓名':['程峥','黄子豪','倪晨阳'],'id':['菜鱼张某','Pangpang','jy_no_hachi'],'段位':['冠绝','冠绝','传奇']}
# dota_df=pd.DataFrame(dota_set)
# print(dota_df)

# 取数，获得series
# print(dota_df['id'])

# 改索引
df=df.set_index('Name')
print(df.head())
print(df['Age'][:5])
print(df['Age'].mean())

# 根据index索引找某行某列的值(列=age，索引修改为姓名了直接输姓名)
# print(df['Age']['Allen, Mr. William Henry'])

#
# df=pd.read_csv('titanic.csv')
# a=df['Age']+10
# print(a)

