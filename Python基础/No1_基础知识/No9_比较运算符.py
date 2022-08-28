# Mmq's Data Science Training
# Created at: 2022/6/25 19:26

# ==比较变量的值，is判断对象的id(存储地点)是否一致
a=[10,20,30,40]
b=[10,20,30,40]
print(id(a),id(b))
print(a==b)
print(a is b)
