class P(object):
    def __init__(self,name):
        self.name=name

    def foo(self):
        print("I am P-foo")
class S(P):
    def __init__(self,age):
        self.age=age
    def par(self):
         super(S, self).foo()
    def foo(self):
        print("I am S-foo")

s=S(11)
s.par()
