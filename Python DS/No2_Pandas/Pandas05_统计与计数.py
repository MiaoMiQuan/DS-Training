import pandas as pd

# 手动指定索引和列
# df=pd.DataFrame([[1,2,3],[4,5,6]],index=['a','b'],columns=['A','B','C'])
# print(df)

# 一元统计
# print(df.sum())
# print(df.sum(axis='rows'))
# print(df.sum(axis=1))
# print(df.sum(axis='columns'))

# 二元统计
df=pd.read_csv('titanic.csv')
# #协方差=E(XY)-x的均值*y的均值
# print(df.cov())
# #相关系数 相关系数=协方差/两个变量的标准差之积
# print(df.corr())
#数各个value个数,ascending升降序，bins按照最大值和最小值之间几等分并分类计数

#value_count计数
# print(df['Age'].value_counts())
print(df['Age'].value_counts(ascending=True,bins=5))
# #count
# print(df['Age'].count(),df['Pclass'].count())