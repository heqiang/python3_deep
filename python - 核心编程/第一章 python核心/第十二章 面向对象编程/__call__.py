from time import ctime,sleep

class Entity(object):
    def __init__(self,func,x,args):
        self.x=x,
        self.args=args
        self.func=func
    def __call__(self,name,delay):
        # self.func(*self.args)
        self.func(name,delay)

def loop(name,delay):
    print("start at：",ctime())
    print("名字是："+name)
    print("延迟是：%s秒"%delay)
    sleep(delay)
    print("end at:",ctime())

e=Entity(func=loop,x=3,args=("hq",2))
e.func(name='ceshi',delay=2)




