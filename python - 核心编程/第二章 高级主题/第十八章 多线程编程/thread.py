import _thread
from time import sleep,ctime

def loop0():
    print("start loop0 at:",ctime())
    sleep(4)
    print("loop0 end at:",ctime())

def loop1():
    print("start loop1 at:",ctime())
    sleep(2)
    print("loop1 end at:",ctime())

def  main():
    print("starting at:",ctime())
    _thread.start_new_thread(loop0,(1))
    _thread.start_new_thread(loop1,(2))
    #阻止主线程的继续执行
    sleep(6)
    print("main thread end at :",ctime())

if __name__ == '__main__':
    main()