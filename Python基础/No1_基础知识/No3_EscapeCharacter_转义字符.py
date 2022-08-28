# Mmq's Data Science Training
# Created at: 2022/6/25 13:23

# \n 换行
# \r 回车(光标回到最初)
# \t 制表符-凑满X个四个空格的位置：如hello\t则补三个，hell\t则补4个
# \b 退格

print('Hello\nWorld')
print('-------')
print('Hello\rWorld')
print('-------')
print('Hello\tWorld')
print('-------')
print('Hello\bWorld')
print('-------')

# 用 转义字符 防止单引号嵌套报错
print('Mike:\'I love u.\'')
# 用 双引号 防止单引号嵌套报错
print("Mike:'I love u.'")
# 用连续\\保留一个\
print('\\\\')

# 用原字符去掉转义字符的作用
print(r'hello\nworld')





