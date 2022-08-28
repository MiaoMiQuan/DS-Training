# Mmq's Data Science Training
# Created at: 2022/8/6 22:25
# dir()查看现有的属性方法
print(dir(object))
# 一般重写__str__方法，print对象时可以直接输出特定内容，（如对类的描述），否则会输出XXX object at XXX地址
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_info(self):
        print('You are {0} at age {1}'.format(self.name,self.age))
    def __str__(self):
        return 'You are {0} at age {1}'.format(self.name,self.age)
person1=Person('mmq',20)
print(person1)