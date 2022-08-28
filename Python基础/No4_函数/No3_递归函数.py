# Mmq's Data Science Training
# Created at: 2022/7/16 23:20

def factorial(num):
    if not isinstance(num,int):
        # print('请输入正整数')
        return ('请输入正整数')
    elif num<=0:
        # print('请输入正整数')
        return ('请输入正整数')
    else:
        if num>1:
            return num*factorial(num-1)
        if num==1:
            return 1

print(factorial(3))
print(factorial(4))
print(factorial(0))
print(factorial(-3))
print(factorial('abc'))
