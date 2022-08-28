# Mmq's Data Science Training
# Created at: 2022/8/10 21:59

# with可以自动管理上下文资源，无论什么时候关闭with语句，都将自动关闭文件并释放资源
with open('test01.txt','r+') as file:
    print(file.readlines())
