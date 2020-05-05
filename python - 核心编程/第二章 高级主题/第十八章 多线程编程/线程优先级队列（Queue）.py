import threading
import time
from threading import  Lock
import queue
threadLock=Lock()
exitFlag=0
class myThread(threading.Thread):
        def __init__(self,threadID,name,q):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.q = q
        def run(self):
            print("线程开启：%s"%(self.name))
            process_date(self.name,self.q)
            print("线程结束：%s" %(self.name))

def process_date(threadName,q):
    while not exitFlag:
            threadLock.acquire()
            if not workQueue.empty():
                data=q.get()
                threadLock.release()
                print("%s processing %s"%(threadName,data))
            else:
                threadLock.release()
            time.sleep(1)
threadList=["Thread -{}".format(i) for i in range(1,4)]
nameList= ["One", "Two", "Three", "Four", "Five"]

#创建大小为10的队列
workQueue=queue.Queue(10)
threads=[]
threadID=1

#创建新线程
for tName in threadList:
    thread=myThread(threadID,tName,workQueue)
    thread.start()
    #将创建好的线程放入列表
    threads.append(thread)
    threadID += 1

#队列填充
threadLock.acquire()
for word in nameList:
    workQueue.put(word)
threadLock.release()

#等待队列清空
while   workQueue.empty():
        pass

#通知线程是时候退出
exitFlag=1

#等待所有线程结束
for t in threads:
    t.join()
print("退出主线程")

