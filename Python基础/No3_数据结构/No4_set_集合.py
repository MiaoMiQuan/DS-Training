# Mmq's Data Science Training
# Created at: 2022/7/5 22:09

# 元组：无序、可变(不能增删改)、可迭代，相当于没有value的字典,元素不重复
# 创建：可以用，结尾，不填满;用set()将其他形式转变为set
print('---------------------------创建---------------------------')
set0={'a','b','c','a','b','c'}
print(set0)
set1=set(range(5))
print(set1)
set2=set('python')
print(set2)

lst=list('python')
print(lst)

# 增：add(加一个)、update(迭代加，加至少一个)
print('---------------------------增加---------------------------')
s={10,20,30,40,50,60}
s.add(70)
print(s)
s.update({70,80})
print(s)
s.update([90,100])
print(s)
s.update((110,120))
print(s)

# 删除：remove(删除一个特定元素,没有则抛异常)、discard(删除一个特定元素,没有则啥都不抛)、pop(删除栈顶元素)、clear(清空集合)、del(删除集合)
print('---------------------------删除---------------------------')
s.remove(120)
print(s)
s.discard(120)
print(s)
s.discard(110)
print(s)
s.pop()
print(s)
s.clear()
print(s)
del s

# 集合关系:相等、是否子集、是否超集、是否无交集
print('---------------------------集合关系---------------------------')
s1={10,20,30}
s2={10,20,30}
print(s1==s2)

s1.add(40)
print(s2.issubset(s1))
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s2.issuperset(s1))
print(s1.isdisjoint(s2))

# 集合操作:相等、是否子集、是否超集、是否无交集
print('---------------------------集合操作---------------------------')
s1={1,2,3,4,5}
s2={3,4,5,6,7}
print(s1.intersection(s2),s1&s2)
print(s1.union(s2),s1|s2)
print(s1.difference(s2),s1-s2)
print(s1.symmetric_difference(s2),s1^s2)

# 集合生成式
print('---------------------------生成式---------------------------')
set={i**2 for i in range(5)}
print(set)
