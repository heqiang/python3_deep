# attr()系列函数可以在各种对象下工作，不限于类（class）和实例（instances）
# hasattr()函数为Boolean 类型 它的目的就是为了决定一个对象是否有一个特定的属性，一般用于访问某属性前先作一下检查
# getattr()和 setattr()函数相应地取得和赋值给对象的属性，
# getattr()会在你试图读取一个不存在的属性时，引发 AttributeError 异常，除非给出那个可选的默认参数
# setattr()将要么加入一个新的属性，要么取代一个已存在的属性。
# 而 delattr()函数会从一个对象中删除属性。


class myClass(object):
    def __init__(self):
        self.foo=100

myInt=myClass()
print(hasattr(myInt, 'foo'))#查看是否有foo属性
print(getattr(myInt, 'foo')) #获取该属性的值
print(getattr(myInt, 'bar', 'opps')) #获取一个不存在的属性 并给一个默认值
setattr(myInt,'bar','my attr')  #加入一个新的属性并赋值
print(dir(myInt)) #利用dir()函数列出该模块或者对象的所有属性信息
print(getattr(myInt, 'bar'))
delattr(myInt,'foo')  #删除foo 属性
print(getattr(myInt, 'foo'))
print(myInt.foo)

