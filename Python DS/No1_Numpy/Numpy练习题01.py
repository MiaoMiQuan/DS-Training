# Mmq's Data Science Training
# Created at: 2022/8/17 20:15
import numpy as np
1.
print(np.__version__)
2.
print(np.zeros((3,3)).nbytes)
3.
# print(help(np.info(np.add)))
4.
array=np.arange(10,50)
print(array[::-1])
5.
print(np.nonzero(np.array([1,0,2,5,0,3])))
array=np.array([1,0,2,5,0,3])
print(np.argwhere(array!=0))
6.
array=np.random.rand(3,3)
print(array.min(),array.max())
7.
array=np.ones((5,5))
print(np.pad(array,pad_width=1,constant_values=0)) #pad包裹
8.
array=np.random.rand(6,7,8)
print(np.unravel_index(100,array.shape))
9.
array=np.random.rand(5,5)
print((array-array.min())/(array.max()-array.min()))
10.
a1=np.array([0,1,2,3,4])
a2=np.array([0,1,2,3,5])
print(np.intersect1d(a1,a2)) #intersec找相同值
11.
print(np.datetime64('today','D'),np.datetime64('today','M'))  #今天
print(np.datetime64('today','D')-np.timedelta64(1,'D'))  #昨天
12.
print(np.arange('2021-07-01','2021-07-20',dtype='datetime64'))
13.
array=np.random.rand(100).reshape((10,10))
print(array)
print(np.floor(array))
