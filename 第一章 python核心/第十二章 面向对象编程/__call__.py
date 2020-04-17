from time import ctime,sleep
class Entity(object):
    def __init__(self,func,x,args):
        self.x=x,
        self.args=args
        self.func=func
    def __call__(self):
        self.func(*self.args)

def loop(name,delay):
    print("start at：",ctime())
    print(name)
    print(delay)
    sleep(delay)
    print("end at:",ctime())

e=Entity(func=loop,x=3,args=("hq",2))
print(e.func)



