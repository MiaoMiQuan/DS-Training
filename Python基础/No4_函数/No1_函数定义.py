# Mmq's Data Science Training
# Created at: 2022/7/14 18:37

# 函数返回值如果有多个，则组成一个元组

print('函数参数的定义'.center(60,'-'))
# 默认形参
def default_formal_argument(a,b=100):
    return a,b

print(default_formal_argument(10))
print(default_formal_argument(10,20))
print(default_formal_argument(a=10,b=100))

# 同时定义位置和关键字形参时，位置形参在前(名字可以不用args，带对应数量的*即可)
print('无法事先确定需要传的位置实参的个数时，用*args，结果为一个元组'.center(60,'-'))
def try_args0(*args):
    print(args)
    print(args[0])

def try_args1(**args):
    print(args)
    print(args['a'])
try_args0(10,20,30)
print('无法事先确定需要传的关键字实参的个数时，用**args，结果为一个字典'.center(60,'-'))
try_args1(a=10,b=20,c=30,d=40,e=50)

print('利用*的位置形参函数调用方法'.center(60,'-'))
def try_args(a,b,c):
    print(a,b,c)
lst=[10,20,30]
print(try_args(*lst)) #每个元素当成位置实参传入

print('利用**的位置关键字函数调用方法'.center(60,'-'))
dic={'a':100,'b':200,'c':300}
print(try_args(**dic)) #每个键值对当成关键字实参传入

def shican(a,b,*,c,d) #表示a、b可以用位置、关键字形式传参，而c、d只能用关键字传参
