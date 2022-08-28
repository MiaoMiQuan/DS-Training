# Mmq's Data Science Training
# Created at: 2022/8/13 21:36
import numpy as np

array=np.array([1,2,3,4,5])
print(array)

# 矩阵填充
array.fill(0)
print(array)

# 多维矩阵
array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array)
print(array.ndim)

# 多维矩阵取值
print(array[1]) #取一行
print(array[:,1]) #取一列
print(array[1,1]) #取单个值
print(array[0:2,1]) #取多行的一列
print(array[1,0:2]) #取多列的一行

# array的复制，用array2=array1.copy()

# arange构造等差数组
array=np.arange(0,100,10)
print(array)

# 用boolen来取值，哪些要哪些不要
array1=np.array([1,2,3,4,5])
array2=np.array([0,1,0,1,0],dtype='bool')
print(array1[array2])

