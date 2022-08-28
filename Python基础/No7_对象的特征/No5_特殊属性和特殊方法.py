# Mmq's Data Science Training
# Created at: 2022/8/7 14:50

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_info(self):
        print('You are {0} at age {1}'.format(self.name,self.age))
    def __str__(self):
        return 'You are {0} at age {1}'.format(self.name,self.age)

person1=Person('mmq',20)
# __dict__获得类或实例对应的所有属性的字典
print(person1.__dict__)
# __class__获得所属的类
print(person1.__class__)
# __bases__获得某一个class的父类
print(Person.__bases__)
# __subclasses()获得一个class的子类
print(object.__subclasses__())

# __len__重新定义长度方法
# __add__重新定义相加方法，比如把字符串的相加定义为相连
# __new__用于创建对象。在对象创建之前被调用，任务是创建该对象并返回该实例对象，是静态方法。
# __init__用于对创建的对象进行初始化，在对象创建之后被调用，设置对象的一些初识属性值