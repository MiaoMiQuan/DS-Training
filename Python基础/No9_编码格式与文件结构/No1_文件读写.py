# Mmq's Data Science Training
# Created at: 2022/8/8 23:07

file=open('test01.txt','r+')
print(file.readline())
print(file.readlines())
file.close()

# r只读（指针在开头）,r+读写(覆盖写),不创建,不存在则报错
# w只写,w+读写,存在则覆盖,不存在则创建,都会将旧文件清零，指针在开头
# a写(附加写),a+读写(附加写),有则继续写,没有则创建，指针在结尾
# b，以二进制打开文件，需与r、w、a结合使用，不能单独使用
