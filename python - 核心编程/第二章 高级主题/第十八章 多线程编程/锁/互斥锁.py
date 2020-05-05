#一般的锁和互斥锁的区别
    #当嵌套使用的时候 使用Lock 会出现卡死  而Rlock不会
    #RLock是通过计数来实现对锁的控制的，acquire一次 ,count+=1  release一次 count-=1
    #当count=0时 所有的线程就可以对锁进行抢夺
from  threading import  Thread ,Lock,RLock,current_thread
import time
a=b=RLock()

class myThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name=name
    def run(self):
       f1(self.name).go()
       f2(self.name).go()
class f1(object):
    def __init__(self,name):
        self.name=name
    def go(self):
        a.acquire()
        print("%s拿到A锁"%(self.name))
        b.acquire()
        print( "%s拿到B锁"%(self.name))
        a.release()
        b.release()
class f2(object):
    def __init__(self,name):
        self.name=name
    def go(self):
        a.acquire()
        print("%s拿到A锁"%(self.name))
        b.acquire()
        print( "%s拿到B锁"%(self.name))
        a.release()
        b.release()

if __name__ == '__main__':
    for x in range(3):
        t=myThread(x)
        t.start()
        t.join()