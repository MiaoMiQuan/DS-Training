# Mmq's Data Science Training
# Created at: 2022/6/26 23:27

# if else的简写
a=10
b=20
c=(a-b if a>0 else b-a)
print(c)

# pass 什么都不做,当做占位符

# range
r=range(0,10,1)
print(r,list(r))
r=range(10,0,-1)
print(r,list(r))
r=range(10,0,1)
print(r,list(r))

dic={0:'a',1:'b',2:'c',3:'d'}
# For循环，要是可迭代对象如range、list、tuple、dictionary、string
for i in dic:
    print(dic[i],sep='',end='')
# for循环中，如迭代对象(i)在程序中不需要用到,也可以用下划线代替
for _ in range(5):
    print('abc')

# break 结束for in / while循环，通常与if一起用
# continue 结束这次for in / while循环，进入下一次循环，通常与if一起用
# for..else / while...else,当循环结束or不满足循环条件且没被break,进入else
a=0
while a<10:
    a+=1
else:
    print(a)

a=10
while a<20:
    break
else:
    print('a<20')

for i in range(3):
    print(i)
else:
    print(100)