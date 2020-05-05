# 事件 Event类
    # set()默认为False当被调用的时候其值变为True
    # is_set() 判断是否设置了falg
    # clear() 将flag设置为False
    # wait()会一直监听flag 如果没有监听到flag  就会一直处于阻塞的状态


from threading import Thread,Event,current_thread
import time
e = Event()


def traffics_lights():
    time.sleep(5)
    e.set()
    e.clear()
    if t :
        print("true")
    else:
        print("false")
def cars(name):
    print("%s is waiting"%name)
    #程序遇到wait时开始挂起 当wait接收到程序set()值为true时开始由挂起到执行
    e.wait()
    print("%s is running" % name)

if __name__ == '__main__':
    for x in range(10):
        t=Thread(target=cars,args=(x,))
        t.start()
        #声明一个信号线程
    traffics_lights=Thread(target=traffics_lights,)
    traffics_lights.start()