# Mmq's Data Science Training
# Created at: 2022/8/13 22:03
import numpy as np

# 随机数
print('随机数'.center(40,'-'))
random_array=np.random.rand(10) #rand，随机产生几个0-1的数
print(random_array)

random_array_bool=random_array > 0.5 #判断是否满足特定条件（如大于0.5），返回一个array
print(random_array_bool.shape)
print(random_array[random_array_bool]) #用boolen判别，从而只保留满足特定条件的array元素（如大于0.5）

random_array_index=np.where(random_array>0.5) #判断是否满足特定条件（如大于0.5）,返回一个tuple
print(random_array_index)
print(random_array[random_array_index])


# 数值运算
print('数值运算'.center(40,'-'))
array=np.array([[1,2,3],[4,5,6]])
print(np.sum(array)) #求和
print(np.sum(array,axis=0)) #按行走，按列求和
print(np.sum(array,axis=1)) #按列走，按行求和
#乘法：prod
print(np.prod(array,axis=0))
#min\max
print(np.min(array,axis=0)) #按行走，找每列最小的数
print(np.argmin(array,axis=0)) #按行走，找每列最小位置的索引
#mean平均值，std标准差，var方差
#clip限制上下限
print(np.clip(array,2,4))
#round(decimals)保留小数位数


# 排序
print('数组排序'.center(40,'-'))
array=np.array([[8,1,5],[6,2,4],[7,3,9]])
print(array)
print(np.sort(array)) #默认相当于axis=1
print(np.sort(array,axis=0)) #按行走，对每行排序
print(np.sort(array,axis=1)) #按列走，对每列排序
