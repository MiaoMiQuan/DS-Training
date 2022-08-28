# Mmq's Data Science Training
# Created at: 2022/7/3 23:39

# 字典：无序、可变、可迭代
# 创建
print('---------------------------创建---------------------------')
dic={'a':1,'b':2}
print(dic)
dic1=dict(no1='a',no2='b',no3='c')
print(dic1)

# 取值：[]按键取值，没有则报错。dic.get形式，没有则报none，也可以设置不为none的默认值
print('---------------------------取值---------------------------')
print(dic['a'])
print(dic.get('a'))
print(dic.get('c'))
print(dic.get('c','可以设置默认值'))

# 判断存在、增、删、改
print('--------------------------判断存在、增、删、改---------------------------')
# 判断存在
print('a' in dic)
# 增
dic['c']=3
print(dic)
# 删
del dic['c']
print(dic)
dic.clear()
print(dic)
# 改
dic={'a':1,'b':2}
print(dic)
dic['b']=3
print(dic)

# 获取视图
print('--------------------------获取视图---------------------------')
# keys获取所有key、values获取所有value、items获取所有键值对
keys=dic.keys()
print(keys,type(keys))
print(list(keys))

values=dic.values()
print(values,type(values))
print(list(values))

item_s=dic.items()
print(item_s,type(item_s))
print(list(item_s))

# 遍历
print('--------------------------遍历---------------------------')
for i in dic:
    print(i,dic[i])

# 特点：字典的key是不可变对象（不能用list形式等当做key）。key如果重复，则取后写的。空间可以自动伸缩，是一种空间换时间的结构。

# 生成式:zip打包可迭代对象
print('--------------------------生成式---------------------------')
foods=['hamburger','banana']
prices=[100,200]
dic={food:price for food,price in zip(foods,prices)}
print(dic)




# enumerate函数,对可迭代对象，加序号组成元组对
print('--------------------------enumerate---------------------------')
season=['spring','summer','autumn','winter']
print(season)
num_season=enumerate(season)
print(list(num_season))
num_season1=enumerate(season,start=1)
print(list(num_season1))
for i,season in enumerate(season,start=1):
    print('第',i,'个季节是',season)





