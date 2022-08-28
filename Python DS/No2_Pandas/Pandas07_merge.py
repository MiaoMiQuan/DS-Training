import pandas as pd
# merge操作
# a=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['A','B','C'],index=['a','b','c'])
# print(a)
# b=pd.DataFrame([[3,2,3],[6,5,6],[9,8,9]],columns=['C','D','E'],index=['a','b','c'])
# print(b)
# c=pd.merge(a,b)
# print(c)
# c=pd.merge(a,b,on='C')
# print(c)

# 多列merge,数据一致
# a=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['A','B','C'],index=['a','b','c'])
# print(a)
# b=pd.DataFrame([[3,2,3],[6,5,6],[9,8,9]],columns=['C','B','D'],index=['a','b','c'])
# print(b)
# c=pd.merge(a,b,on='C') #merge时，两个df作为共列的一列，数据最好完全相同。此外两个df中重名的列会被重命名
# print(c)
# c=pd.merge(a,b,on=['B','C'])
# print(c)

# 多列merge,数据不一致
a=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['A','B','C'],index=['a','b','c'])
print(a)
b=pd.DataFrame([[3,2,3],[6,5,6],[10,8,9]],columns=['C','B','D'],index=['a','b','c'])
print(b)
c=pd.merge(a,b,on='C') #两列中的c有不同，则不同的行被去掉了
print(c)
c=pd.merge(a,b,on='C',how='outer',indicator=True) #outer，相当于fulljoin
print(c)