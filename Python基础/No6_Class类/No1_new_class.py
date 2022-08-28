# Mmq's Data Science Training
# Created at: 2022/7/24 19:04

# class的命名，首字母大写，后面小写
class Student:
    # 直接写在类里，称为类属性
    student_source='北京'

    # 初始化方法
    def __init__(self,name,age):
        self.name=name #self.name为实例属性，进行了赋值操作，把name的值赋给实例属性
        self.age=age

    # 类之外定义的，叫函数。类之内定义的，叫方法。这是一个实例方法
    def info(self):
        return '我叫{},今年{}岁'.format(self.name,self.age)

    # 类方法
    @classmethod #类方法标识，里面一般传一个cls
    def classmethod(cls):
        return '调用类方法'

    # 静态方法
    @staticmethod #静态方法标识，里面不写self
    def staticmethod():
        return '调用静态方法'

print('打印Student类的信息'.center(40,'-'))
print(type(Student))
print(id(Student))
print(Student)

print('打印Student类中一个实例的信息'.center(40,'-'))
stu=Student('mmq',26)
print(type(stu))
print(id(stu))
print(stu) #表示stu为在该id地址下的一个object实例，id转换为16进制即为object at后面的字
print(stu.name,stu.age)

# 此两种调用方法，功能相同
print(stu.info())         #对象名.方法名()
print(Student.info(stu))  #类名.方法名(对象名)

# 动态绑定方法
stu.gender='male'
print(stu.gender)
# 动态绑定函数
def show():
    print(123)
stu.show=show()
stu.show