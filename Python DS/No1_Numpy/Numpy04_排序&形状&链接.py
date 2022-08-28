import numpy as np

# 排序
array=np.array([[6,2,8],[4,5,9],[3,1,7]])
print(array)
print(np.sort(array))
# print(np.sort(array,axis=0))
print(np.argsort(array)) #排序后的序列，原来的索引位置。新位置：排序后的位置，数字：该位置的数字原来所在的索引

print(np.linspace(0,9,10)) #生成等间隔序列,最后一个参数为生成的个数
values=np.array([1.5,5.5,9.5])
print(np.searchsorted(np.linspace(0,9,10),values)) #定点寻找，点位

# 数组形状
print('数组形状'.center(40,'-'))
array=np.arange(10) #生成等间隔序列，最后一个参数为步长
print(array,array.shape)
array1=array.reshape(2,5) #行数，列数
print(array1,array1.shape)

array_new_axis=array[np.newaxis,:] #用np.newaxis新增维度
print(array_new_axis.shape)
array_new_axis=array_new_axis.squeeze() #用squeeze去除多余维度
print(array_new_axis.shape)
#ravel、flatten可以把矩阵拉平

array1=array1.transpose() #转置 或者直接.T
print(array1)

# 数组连接
print('数组连接'.center(40,'-'))
array_a=np.array([[1,2,3],[4,5,6]])
array_b=np.array([[7,8,9],[10,11,12]])
array_ab_heng=np.concatenate((array_a,array_b),axis=0) #竖着拼
print(array_ab_heng)
array_ab_shu=np.concatenate((array_a,array_b),axis=1) #横着拼
print(array_ab_shu)

print(np.vstack((array_a,array_b))) #vertical着拼
print(np.hstack((array_a,array_b))) #horizonal着拼



