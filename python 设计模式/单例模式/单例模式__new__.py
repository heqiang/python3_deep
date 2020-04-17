#单例设计模式  确保某一个类只有一个实例存在
import  threading
from time  import sleep ,ctime

class Sin(object):
    def __init__(self,x):
        self.x=x
        sleep(1)

    def __new__(cls, *args, **kwargs):
        if not hasattr(Sin,'_instance'):
            Sin._instance=object.__new__(cls)
        return Sin._instance

sin1=Sin(5)
sin2=Sin(5)


#多线程 实现单例模式
def thread_test(args):
    sin=Sin(args)
    print("目前的对象是 :%s 参数是：%d"%(sin,args))

if __name__ == '__main__':
    threads = []
    # for x in range(20):
    #     t=threading.Thread(target=thread_test)
    #     threads.append(t)
    # print("线程开始 at:%s" % (ctime()))
    # for x in threads:
    #     x.start()
    # for x in threads:
    #     x.join()
    # print("线程结束 at:%s" % (ctime()))
    for i in range(10):
        t = threading.Thread(target=thread_test,args=(i,))
        t.start()