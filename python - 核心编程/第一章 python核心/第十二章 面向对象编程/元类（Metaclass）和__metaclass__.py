from time  import ctime
from warnings import warn
#元类的主要目的就是为了当创建类时能够自动地改变类。
    # 拦截类的创建
    # 修改类
    # 返回修改之后的类
# 关于type
# 1 查看对象的类型
# 动态的创建一个类  type(类名, 由父类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)

class FatBoy(object):
    def __init__(self):
        self.name="hq"
    # print("Boy")

class FatBoss(FatBoy):
    ceshi="FatBoss"
    # print('Boss')

boy=FatBoy()
boy.age=15

print(boy.__dict__)
#使用type创建一个实例对象
Test1=type("Test",(),{"ceshi":3}) #添加的属性为类属性 不是实例属性
Test1.foo=2

#创建一个Test的子类
testSon=type("testSon",(Test1,),{})
# print(testSon.ceshi)
# print(testSon.__mro__)

#使用type创建一个带有方法的类
@classmethod
def  sell(self):
    pass
    # print(self.ceshi)
FatGirl=type("fatGirl",(FatBoss,),{"sell":sell})
# print(hasattr(FatGirl, 'ceshi'))
# FatGirl.sell()
FatGirl.sell()
# print(sell.__class__.__class__)
'''
利用函数来定义类
'''
def  upper_attr(class_name,class_parents,class_attr):
        '''
        :param class_name:类名
        :param class_parents: 父类
        :param class_attr: 以字典保存的类属性
        :return: 返回一个类
        '''
        new_attr={}
        for name,value  in class_attr.items():
            print("name =%s and  value = %s" % (name,value))
            if not name.startswith("__"):
                new_attr[name.upper()]=value
                print("大写后的属性名：%s" %(name.upper()))
                print("值是：%s"%(value))
                #利用type创建一个类
        return  type(class_name,class_parents,new_attr)

class  Foo(object,metaclass=upper_attr):
        bar=30

f=Foo()
# print(hasattr(Foo, 'bar'))
# print(hasattr(Foo, 'BAR'))
# print(f.BAR)
'''
利用 class 来定义元类
'''
class UpperAttrMetaClass(type):

    def __new__(cls,class_name, class_parents,class_atts):
        new_attr={}
        for name,value in class_atts.items():
            if not name.startswith("__"):
                new_attr[name.upper()]=value
        def sell(self):
            print("sell")
        new_attr["sell"]=sell
        return type(class_name,class_parents,new_attr)

class Zoo(object,metaclass=UpperAttrMetaClass):
    bar="bip"

z=Zoo()
print(hasattr(Zoo, 'bar'))
print(hasattr(Zoo, 'BAR'))
print(z.BAR)
z.sell()

