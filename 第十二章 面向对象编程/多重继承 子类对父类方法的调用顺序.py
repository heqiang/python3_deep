#! /usr/bin/python
# -*- coding:utf-8 -*-

'''
经典类 : 深度优先 从左至右
新式类 ：广度优先

'''
class P1(object):
    def foo(self):
        print( 'p1-foo')
    def bar(self):
        print("p1-bar")


class P2(object):
    def foo(self):
        print('p2-foo')

    def bar(self):
        print('p2-bar')

class C1(P2, P1):
    pass

class C2(P2, P1):
   pass

class D(C1, C2):
    pass

if __name__ == '__main__':
    print(D.__mro__)  # 只有新式类有__mro__属性，告诉查找顺序是怎样的
    d = D()
    d.foo()
    d.bar()