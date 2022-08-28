# Mmq's Data Science Training
# Created at: 2022/7/6 22:26

# 字符串不可变
# 字符串滞留机制：如果a和b的字符串内容相同，则指向同一个地址
a = 'python'
print(id(a))
b = 'python'
print(id(b))
c = 1
d = 1
print(id(c), id(d))

# a is b 比较内存地址(id)，a=b 比较内容(value)

# 字符串链接：.join(),比用+更省内存

# 查找：index()查找第一次出现的位置，不存在则报错；rindex()查找最后一次出现的位置，不存在则报错；
# find()查找第一次出现的位置，不存在则返回-1；rfind()查找最后一次出现的位置，不存在则返回-1；
print('---------------------------查找---------------------------')
str0 = 'ilovepythonpython'
print(str0.index('python'))
print(str0.rindex('python'))
print(str0.find('ooo'))
print(str0.rfind('ooo'))

# 大小写转换，转换后产生新字符串
print('---------------------------大小写转换---------------------------')
str0 = 'iLovePython'
# 全大写
print(str0.upper())
# 全小写
print(str0.lower())
# 全首字母大写，其余全小写
print(str0.capitalize())
# 大写、小写交换
print(str0.swapcase())
# 每个单词第一个字母大写，其余全小写
print(str0.title())

# 对齐,若指定宽度小于原字符串，则返回字符串本身
print('---------------------------字符串对齐---------------------------')
print(str0.center(20, '-'))
print(str0.ljust(20, '-'))
print(str0.rjust(20, '-'))
print(str0.zfill(20))

# 劈分，split左起劈分，rsplit右起劈分，分隔的字符不会出现
print('---------------------------字符串劈分---------------------------')
print(str0.split(sep='o'))
print(str0.split(sep='o',maxsplit=1))
print(str0.split('o',2))
print(str0.split('z',1))
print(str0.rsplit('o',1))
print(str0.rsplit('o',2))
print(str0.rsplit('z',1))

print('字符串常用操作'.center(60,'-'))
str0='abc123ilovepython'
# 判断字符串是否由合法标识符组成
print(str0.isidentifier())
# 判断字符串是否全部由空格、回车、换行组成
print(str0.isspace())
# 判断字符串是否全部由字母组成
print(str0.isalpha())
# 判断字符串是否全部由数字组成
print(str0.isnumeric())
# 判断字符串是否全部由十进制数字组成
print(str0.isdecimal())
# 判断字符串是否全部由数字或字母组成
print(str0.isalnum())

print('替换与合并'.center(60,'-'))
str0='ilovepythonpythonpython'
# replace,生成新的字符串，替换前的字符串不发生变化
str1=str0.replace('python','java',2)
print(str1)
# join,链接某个list或tuple的所有元素；或链接某个string的全部片段
lst=['i','love','python']
str2='+'.join(lst)
print(str2)
str3=','.join(str2)
print(str3)

print('字符串比较'.center(60,'-'))
# 逐个字符比较，比较的是ord(Unicode)

print('字符串切片'.center(60,'-'))
# 切片产生新字段
print(str0)
print(str0[:3],str0[7:],str0[3::2])
print(str0[:3]+'!'+str0[7:]+str0[3::2])

print('格式化字符串'.center(60,'-'))
# %作为占位符
str0='我叫{},今年{}岁'.format('Mmq',26)
print(str0)
str1='我叫%s,今年%d岁' % ('Mmq',26)
print(str1)

# d前的数字表示整体的宽度
print('%20d' % (123456789))
print('%10f' % (3.1415926))
# .3表示小数点后三位
print('%.3f' % (3.1415926))
print('{0:.3}'.format(3.1415926))
print('{0:.3f}'.format(3.1415926))
