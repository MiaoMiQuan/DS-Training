# Mmq's Data Science Training
# Created at: 2022/7/4 23:35

# 元组：无序、不可变(不能增删改)、可迭代
# 创建：可以用，结尾，不填满
print('---------------------------创建---------------------------')
tuple0=(1,2,3)
print(tuple0)
tuple1=tuple((1,2,3))
print(tuple1)
tuple2=(1,2,)
print(type(tuple2))

# 元组存储的是对象的引用。所以，你不能修改为引用其他对象；但若对象本身可变，你可以修改对象
tuple3=(0,[1,2],3)
print(tuple3)
tuple3[1].append(4)
print(tuple3)