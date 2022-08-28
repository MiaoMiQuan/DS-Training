import numpy as np
#数组读取
#python用法
with open('data.txt') as file:
    data=[]
    line_num=0
    for lines in file.readlines():
        num_list=lines.split()
        for num in num_list:
            data.append(int(num))
        line_num+=1
    array=np.array(data)
    array=array.reshape(line_num,int(array.size/line_num))
print(array)

#numpy用法
file=np.loadtxt('data.txt',delimiter=' ',skiprows=0) #直接读取，设置分隔符，设置是否跳过行，usecols使用哪几列
print(file)
array_npy=np.load('array.npy')
print(array_npy)


#数组保存
array=np.array([[1,2,3],[4,5,6]],dtype=int)
np.savetxt('array.txt',array,fmt='%d',delimiter=',')
np.save('array.npy',array) #保存为文件
np.savez('array.npz',a=array) #保存为压缩文件
load_array=np.load('array.npz') #load读取压缩文件
print(load_array.keys()) #压缩文件用字典表示
print(load_array['a'])