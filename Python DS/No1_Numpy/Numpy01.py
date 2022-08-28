# Mmq's Data Science Training
# Created at: 2022/8/13 16:00
import numpy as np

# array定义
array=np.array([1,2,3,4,5])
array=np.array([0,1,0,1,0],dtype='np.float32') #创建同时改变类型
print(array)

# 查看array的类别、形状、数量
print(array.dtype) #array的类别，一个array的类型必须一致，如果int+float则全变float，加string则变str
print(array.shape) #array的形状
print(array.itemsize) #单个元素占字节数，int占4个字节，float占8个字节
print(array.nbytes) #查看总共占多少字节
print(array.size) #array的元素数
print(array.ndim) #查看是几维矩阵

# 类别转化
array=array.astype(np.float64)
print(array.dtype)
print(array)

# 基础运算
array+=1
print(array)
array_sum=array*2
print(array_sum)
array_multi=array*array
print(array_multi)

# 取定位值
print(array_multi[2])
print(array_multi[2:4])
