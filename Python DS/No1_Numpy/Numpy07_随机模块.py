import numpy as np

#设置打印精度
np.set_printoptions(precision=3)
#设定种子
np.random.seed(100)

a=np.random.rand(3,2) #所有值在0-1的随机分布，参数为矩阵
print(a)
b=np.random.randint(10,size=(3,2)) #随机正整数
print(b)
c=np.random.normal(0,1,10) #随机正态分布
print(c)
d=np.random.randn(3,2) #一组符合标准正态分布的概率分布
print(d)

#洗牌
to_shuffle=np.arange(10)
np.random.shuffle(to_shuffle)
print(to_shuffle) #shuffle洗牌