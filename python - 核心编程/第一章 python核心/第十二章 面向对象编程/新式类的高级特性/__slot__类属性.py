# __slots__ 指定了该类的实例属性集合 不能创建没有在改列表内的属性
#它能防止用户随心所欲的动态增加实例属性。带__slots__属性的类定义不会存在__dict__了（除非你在__slots__中增加'__dict__'元素）
class  Slott(object):
    __slots__ = ("foo",'bar')

sl=Slott()
sl.foo=200
print(getattr(sl, 'foo'))
sl.bb=22  # output   'Slott' object has no attribute 'bb'
