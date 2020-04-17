from warnings import warn

# 定义元类 ReqStrReper
class  ReqStrReper(type):

    def __init__(self,name,bases,attrd):
        super().__init__(name,bases,attrd)
        if '__str__' not in attrd:
            raise TypeError("Class requires overried of  __str__()")
        if '__repr__' not in  attrd:
            warn("class  suggest overried of __repr__()\n",stacklevel=3)
#定义一个成功的类
class  Foo(object,metaclass=ReqStrReper):

    def __str__(self):
        return ("Instarnce of class",self.__class__.__name__)

    def __repr__(self):
        return self.__class__.__name__
f=Foo()

#定义一个只有__str__或者__repr__的类
class Bar(object,metaclass=ReqStrReper):

    def __str__(self):
        return self.__class__.__name__
b=Bar()
print(b.__str__())