# Mmq's Data Science Training
# Created at: 2022/6/28 23:56

# 列表：有序、可变、可迭代
# list的索引，左一为0，右1为-1
# list实际储存的是每个元素的id
# 列表的创建,lst=['a','b']或lst=list(['A','B'])/lst=list('python')则会把每个字母分开
# 已知值找索引,lst.index,可标明查找范围，找不到则会报错
lst=['a','b','a','c','d']
print(lst.index('a'))
print(lst.index('a',1,4))
# 已知索引，找值
print(lst[2],lst[-2])
# 切片
print(lst[1:4:2])
print(lst[4:1:-1])

# 增：append(整体当一个添加)、extend(迭代添加)、insert(任意位置加一个)、切片(任意位置的内容替换为另一堆可不等长的内容)
print('---------------------------增加---------------------------')
lst.append('e')
print(lst)
lst.append(['e','f'])
print(lst)
lst.extend(['f','g'])
print(lst)
lst.insert(1,['z','z'])
print(lst)
lst[1:3]=['c','c','c','c']
print(lst)

# 删除：remove(删除第一个特定值)、pop(删除指定索引上的值)、切片(任意位置的内容替换为另一堆可不等长的内容)、clear(清空列表)、del(删除列表)
print('---------------------------删除---------------------------')
lst.remove('c')
print(lst)
lst.pop(1)
lst.pop(-1)
print(lst)
lst[3:6]=[]
print(lst)
lst.clear()
print(lst)
lst=[1,2,3]
del lst

# 修改：用索引修改(通常是把一个位置的值替换为另一个值)、用index找值对应的索引并修改值(通常是把一个特定值替换为另一个值)、切片修改
print('---------------------------修改---------------------------')
lst=[10,20,30,40,50]
print(lst)
lst[-1]=60
print(lst)
lst[lst.index(10)]=5
print(lst)
lst[2:3]=[100]
print(lst)

# 修改：lst.sort()，原列表改变//调用sorted函数，原列表不改变
print('---------------------------排序---------------------------')
lst=[30,20,35,40,50]
print(lst)
lst.sort(reverse=True)
print(lst)
lst1=sorted(lst)
print(lst1)

# 列表生成式
print('---------------------------生成式---------------------------')
lst=[i**2 for i in range(5)]
print(lst)
