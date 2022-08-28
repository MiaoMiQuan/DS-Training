# Mmq's Data Science Training
# Created at: 2022/8/9 22:51

# read(size),读size个长度，若不写则为全部
file=open('test01.txt','r')
print(file.read())
file.close()
file=open('test01.txt','r')
print(file.read(4))
file.close()

# readline,读取一行内容
print('-----------------------------------')
file=open('test01.txt','r')
print(file.readline())
file.close()

# readlines，读取所有行，每行当做一个字符串，放到列表中
print('-----------------------------------')
file=open('test01.txt','r')
print(file.readlines())
file.close()

# write,写一个单元
print('-----------------------------------')
file=open('test01.txt','a+')
file.write('\n12345678')
file=open('test01.txt','r')  #这里重新读取，注意指针位置的变化(读是从指针位置开始读的)
print(file.readlines())
file.close()

# writelines，把一个列表的内容全部写入
print('-----------------------------------')
file=open('test01.txt','a+')
lst=['\n123456789','\n1234567890']
file.writelines(lst)
file=open('test01.txt','r')  #这里重新读取，注意指针位置的变化(读是从指针位置开始读的)
print(file.readlines())
file.close()

# seek，移动文件指针,offset代表位移几个，whence代表从哪里开始(0从头，1从当前位置，2从尾)
print('-----------------------------------')
file=open('test01.txt','r')
file.seek(2,0)
print(file.readlines())
file.close()

# tell，返回文件指针当前位置
print('-----------------------------------')
file=open('test01.txt','r')
file.readline()
print(file.tell())
file.close()

# flush,缓冲区的内容写入文件，但不关闭文件

# close,缓冲区的内容写入文件，同时关闭文件，释放内存