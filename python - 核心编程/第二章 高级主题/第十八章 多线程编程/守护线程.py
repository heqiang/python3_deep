from threading import Thread
from  time  import ctime,sleep

def loop(n):
    print("Start ...at：",Thread.name,ctime())
    while n > 0:
        n-=1
        print(n)
    print("End ...at：", Thread.name, ctime())

if __name__ == '__main__':
    print("主线程开始了,at:", ctime())
    for x in range(6):
        t=Thread(target=loop,args=(15,),name="线程{0}".format(x))
        t.daemon=True
        t.start()
      # t.join()
    print("主线程结束，at：",ctime())