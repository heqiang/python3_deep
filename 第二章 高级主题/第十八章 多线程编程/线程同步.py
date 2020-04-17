import  threading
import time
from threading import Lock

threadLock=Lock()

class myThread(threading.Thread):
    def __init__(self,threadID,thredName,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.thredName=thredName
        self.counter=counter
    def run(self):
        print("线程开始 ："+self.thredName)
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        threadLock.release()

def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print("%s:%s"%(threadName,time.ctime(time.time())))
        counter-=1
threads=[]

#创建新线程
thread1=myThread(1,"thread1",1)
thread2=myThread(2,'thread2',2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t  in threads:
    t.join()
print("退出主线程")
