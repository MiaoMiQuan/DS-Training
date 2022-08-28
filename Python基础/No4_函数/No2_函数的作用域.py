# Mmq's Data Science Training
# Created at: 2022/7/16 23:05

# 局部变量：函数内定义的变量，用global可变为全局变量
# 全局变量：函数外定义的变量，作用于全局
print('局部变量c'.center(60,'-'))
def part(a,b):
    c=a+b
    print(c)
part(10,20)
# print(c)

print('全局变量d'.center(60,'-'))
d=100
def glo(a,b):
    d=a/b
    print(d)
    print('函数内print d:',d)
glo(d,d)
print('函数外print d:',d)

print('全局变量c'.center(60,'-'))
def part_glo(a,b):
    global c
    c=a+b
    print('函数内print c:',c)
part_glo(10,20)
print('函数外print c:',c)
