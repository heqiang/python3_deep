# property 装饰器 是对私有属性的一个保护 有获取 重新赋值 删除等属性
#在属性前加一个下划线表示私有属性
class  Person(object):
    def __init__(self,name,age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return  self._name
    @property
    def age(self):
        return  self._age
    @name.setter
    def name(self,value):
        if not  isinstance(value,str):
            raise  TypeError("Excepted a string")

        self.name = value
    @name.deleter
    def name(self):
        raise AttributeError("can't  delete attribute")
    @age.setter
    def age(self,value):
        if value <=0:
            print("年龄最小不能小于0")
        self._age=value
    @age.deleter
    def age(self):
        raise  AttributeError("can't delete attribute")
    
p = Person("hq",12)
print(p.name)
p.age=0
print(p.age)

