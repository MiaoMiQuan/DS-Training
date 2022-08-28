import numpy as np

# 1. 把array设为不能改写
z=np.zeros((3,3))
z.flags.writeable=False #不能改写
z.flags.writeable=True
# z[0]=1

# 2. 查看array中离某个数最近的数
z=np.random.rand(100)*100
num=np.random.rand()*100
print(num)
rest=abs(z-num)
print(np.argmin(rest))
print(num,z[np.argmin(rest)])

# 3. 查看数组位置和对应多值
z=np.arange(9).reshape(3,3)
for index,value in np.ndenumerate(z):
    print(index,value)

# 4. #按某一列的顺序排列数组
z=np.random.randint(0,10,(3,3))
print(z)
print(z[[1,2,0]]) #行交换
print(z[:,[1,2,0]]) #列交换
print(z[:,-1].argsort())
print(z[z[:,-1].argsort()])

# 5. 查看元素出现的次数
z=np.random.randint(0,3,(3,3)).flatten()
print(np.bincount(z)) #数元素个数,index是元素，value是该元素出现的次数

# 6. 对多行序列多最后两行求和
z=np.random.randint(0,10,(4,4))
print(z)
print(z[-2:].sum())

# 7. 对多维序列多最后两维求和
z=np.random.randint(0,10,(4,4,4,4))
print(z.sum(axis=(-2,-1)))

# 8. 找array里最大k个数
z=np.arange(5)
np.random.shuffle(z)
print(z)
k=3
max_k_arg=np.argpartition(z,kth=3) #比第k个数大大数在右边，比第k个数小的数在左边，返回新序列在原序列的索引值
max_k=np.partition(z,kth=3) #比第k个数大大数在右边，比第k个数小的数在左边，返回序列
print(max_k_arg)
print(max_k)
print(max_k[-k:],z[max_k_arg][-k:])

# 9.看每一行是否正反相同
a=np.array([1,2,3,4,5])
b=np.array([1,2,3,4,6])
print(np.all(a==b),np.any(a==b))

array=np.random.randint(0,10,(5,3))
print(array)
print(np.all(array==array[:,-1::-1],axis=1))