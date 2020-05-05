'''
super() 可理解为在内嵌一个函数 继承父类的函数的同时必须得写上相应的形参
'''
class  Parent(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bar(self,message):
        if message=="hello":
            print("hello")
        else:
            print("thanks")

class  Son(Parent):
    def __init__(self,name,age,sex):
        super().__init__(name,age)
        self.sex=sex
    def bb(self,message):
        super().bar(message)
        if message=="ss":
            print("Son  bb")
        else:
            print("son  other")



a=Son("hq",15,"女")
a.bb("ss")
'''
实例
'''
class SortedKeyDict(dict):
    def keys(self):
        return  sorted(super().keys())#sorted(self.keys())

d=SortedKeyDict((('zheng-cai', 67), ('hui-jun', 68),('xin-yi', 2)))
print(d.keys())