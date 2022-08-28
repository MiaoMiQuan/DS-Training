# Mmq's Data Science Training
# Created at: 2022/8/6 16:41

# 用class封装数据和行为，在类对象外部调用方法，形成了隔离。若该属性不希望在类对象外部被调用，则属性前面使用"__"
class student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get_info(self):
        return self.name,self.__age

stu=student('mmq',25)
print(stu.get_info())
print(stu.name)
# 加了__就访问不了
# print(stu.__age)
# 也可以通过这种方式强行访问
print(stu._student__age)

