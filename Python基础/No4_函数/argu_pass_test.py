# Mmq's Data Science Training
# Created at: 2022/7/14 22:36
def pass_test(num,lst):
    num=100
    lst.append(40)
    print(num)
    print(lst)
    return

# 若为可变对象，则函数体内的修改会影响函数外的值；不可变对象则不会影响
a=1
b=[10,20,30]
print('原a={},原b={}'.format(a,b))
c=pass_test(a,b)
print('现a={},现b={}'.format(a,b))
