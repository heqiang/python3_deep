from time  import ctime
from warnings import warn
#实例一

class MetaC(type):
    def __init__(cls, name, bases, attrd):
         super().__init__(name, bases, attrd)
         print('*** Created class %r at: %s' % (name, ctime()))

print( '\tClass "Foo" declaration next.')

#元类的实现
class Foo(object,metaclass=MetaC):
      def __init__(self):
          print('*** Instantiated class %r at: %s' % (self.__class__.__name__, ctime()))


print('\tClass "Foo" instantiation next.')
f=Foo()
print("Done")

