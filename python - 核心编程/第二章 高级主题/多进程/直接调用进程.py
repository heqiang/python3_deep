from multiprocessing import Process
import time

def func_pro(name):
    print("目前运行的进程名是：%s"%(name))

if __name__ == '__main__':
    print("stat at:%s"%time.time())
    t1=Process(target=func_pro,args=("hq",))
    t1.start()
    t1.join()
    print("end at :%s"%time.time())