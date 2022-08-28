import pandas as pd
import numpy as np
data=pd.DataFrame(columns=['A','B','C'],data=np.random.randint(5,size=(20,3)))
print(data)

#pandas排序
# ordered_data=data.sort_values(by=['B','C'],ascending=(True,False))
# print(ordered_data)

#pandas去重
# dropped_data=data.drop_duplicates()
# print(dropped_data)
# print(dropped_data.count(),data.count())

#按某一列去重
# dropped_data_a=data.drop_duplicates('A')
# print(dropped_data_a)
# print(dropped_data_a.count(),data.count())

#函数应用
def big_or_small(df):
    if df['A']<3:
        return 'small'
    elif df['A']>=3:
        return 'big'

data['big_or_small']=data.apply(big_or_small,axis='columns')
print(data)

#字典映射
# mapping_dic={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five'}
# data['mapping']=data['A'].map(mapping_dic) #函数内是一个字典
# print(data)

#assign加列

#replace替换
# data=data.replace(to_replace=1,value=11)
# print(data)

#cut离散化分割并重命名
bins_data=pd.cut(data['A'],[-1,1,3,6],labels=['-1~1','1~3','3~6'])
print(bins_data)

#isnull查询每个位置是否是缺失值
#isnull().any(axis=0) 每行是否有缺失值
#df.fillna(5) 有缺失值则填5

