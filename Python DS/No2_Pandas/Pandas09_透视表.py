import pandas as pd

df=pd.read_csv('titanic.csv')

# df_pivot=df.pivot(index='Survived',columns='Pclass',values='Fare') #pivot要求index和column对应的元素单一，即不能同一个index和column组合对应多个不同的value
# print(df_pivot)

df_pivot_table=df.pivot_table(index='Survived',columns='Pclass',values='Fare',aggfunc='sum') #pivot_table则可以对应多个不同的value，选aggfunc即可
print(df_pivot_table)
print(df_pivot_table.sum(axis=0),df_pivot_table.sum(axis=1))
df_pivot_table=df.pivot_table(index='Survived',columns='Pclass',values='Fare',aggfunc='count') #count计数
print(df_pivot_table)

cb=pd.crosstab(index=df['Survived'],columns=df['Pclass']) #用交叉表计数
print(cb)
cb=pd.crosstab(index=df['Survived'],columns=df['Pclass'],values=df['Fare'],aggfunc='sum') #用交叉表求和
print(cb)
