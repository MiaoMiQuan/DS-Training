import numpy as np

print(np.arange(5,10,2))
print(np.linspace(5,10,3))
print(np.logspace(1,5,3,dtype=int)) #对数生成，里面的数为对数的几次方,默认以10为底

print(np.zeros(3))
print(np.ones((3,3)))
print(np.ones((3,3))*8)

a=np.array([1,2,3])
print(a)
a.fill(1) #把所有值全改变
print(a)

b=np.zeros_like(a) #生成跟b一样shape的纯0结构，同理ones_like
print(b)

c=np.identity(3) #单位矩阵
print(c)