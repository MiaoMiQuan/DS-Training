import numpy as np
a=np.arange(1,5)
b=np.arange(0,4)
print(a,b)
print(np.multiply(a,b)) #对位相乘，维度必须一样
print(np.dot(a,b)) #标准的矩阵相乘

print(np.multiply(np.array([[1,2],[3,4]]),np.array([[5,6],[7,8]])))

print(a==b) #逐一对比，每一位是否相等
print(np.logical_and(a,b)) #逻辑与，同理或、非。。