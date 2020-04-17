
#不可变的类属性 只有通过类的访问才能进行修改等操作 通过实例的进行相同属性的赋值时会产生一个新的同名属性 访问时优先访问实例属性
#可变的类属性
class C(object):
    versopn=1
    x={2003:"poe2"}
    y=(2,3,5,6,3)

c=C()
print(c.y)
print(C.y)

z=set()
print(type(z))
print(type(c.y))
