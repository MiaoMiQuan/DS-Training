# Mmq's Data Science Training
# Created at: 2022/8/6 21:37

# class 子类(父类1,父类2):
# 如果没有父类，默认继承object
print('原父类'.center(40,'-'))
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_info(self):
        print('You are {0} at age {1}'.format(self.name,self.age))
person1=Person('mmq',20)
person1.show_info()

# super().xxx()表示子类先执行父类xxx的方法，再继续执行子类方法
print('子类直接继承'.center(40,'-'))
# class Student(Person):
#     def __init__(self,name,age,score):
#         super().__init__(name,age)
#         self.score=score
# stu1=Student('mmq',20,100)
# stu1.show_info()

print('子类部分重写'.center(40,'-'))
# 如果子类对父类的属性或方法不满意，可以重写方法
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score=score
    def show_info(self):
        super().show_info()
        print('but actually you are not')

stu1=Student('mmq',20,100)
stu1.show_info()
print(dir(Student))