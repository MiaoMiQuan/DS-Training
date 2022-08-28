# Mmq's Data Science Training
# Created at: 2022/7/14 19:14
def mmq_sum(a,b):   #此处 a b是形参，位置在函数的定义处
    return a+b

# 传参方式：位置传参
a=mmq_sum(10,20)    #此处 10 20是实参，位置在函数的调用处
print(a)

# 传参方式：关键字传参
a=mmq_sum(b=10,a=20)
print(a)