# Mmq's Data Science Training
# Created at: 2022/6/25 12:45
file=open('D:\DS Workout\Python基础\TXT_to_be_written.txt','a+')
print('Helloworld',file=file)
file.close()

# r只读,r+读写(覆盖写),不创建,不存在则报错
# w只写,w+读写,存在则覆盖,不存在则创建,都会将旧文件清零
# a写(附加写),a+读写(附加写),有则继续写,没有则创建
