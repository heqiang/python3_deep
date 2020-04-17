class myClass(object):
    def __new__(cls, *args, **kwargs):
        t=super().__new__(cls)
        print("new构造器:%d"% id(t))
        return t
    def __init__(self):
        print("init构造器：%d" % id(self))
    def  __str__(self):
        return "this is Class str"

mc=myClass()
print(mc)
print(id(mc))

