# Mmq's Data Science Training
# Created at: 2022/8/7 19:27
import copy
# 浅拷贝,数字
print('浅拷贝,数字'.center(80,'-'))
c=100
a=c
b=c
print(a,id(a),b,id(b),c,id(c))
# c指向新的对象
c=10
print(a,id(a),b,id(b),c,id(c))

# 浅拷贝，列表
print('浅拷贝,列表'.center(80,'-'))
c=[10,20,30]
a=c
b=c
print(a,id(a),b,id(b),c,id(c))
c.append(40)
# c依旧指向原来的对象
print(a,id(a),b,id(b),c,id(c))

# 深拷贝,数字
print('深拷贝,数字'.center(80,'-'))
c=100
a=copy.deepcopy(c)
b=copy.deepcopy(c)
print(a,id(a),b,id(b),c,id(c))
# c指向新的对象
c=10
print(a,id(a),b,id(b),c,id(c))

# 深拷贝，列表
print('深拷贝,列表'.center(80,'-'))
c=[10,20,30]
a=copy.deepcopy(c)
b=copy.deepcopy(c)
print(a,id(a),b,id(b),c,id(c))
c.append(40)
# c依旧指向原来的对象
print(a,id(a),b,id(b),c,id(c))
