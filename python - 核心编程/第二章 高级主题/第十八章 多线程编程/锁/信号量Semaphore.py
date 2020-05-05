#信号量 本质也是一个锁 但是这个锁可以允许多个任务同时执行任务
from  threading import Thread,Semaphore,current_thread
import time
#代表可以执行五个任务 第六个任务要执行的时候 必须等其中一个结束才可以

se=Semaphore(5)


def do_task():
    se.acquire()
    print("%s 获取了权限"%current_thread().name)
    time.sleep(2)
    print("%s 放弃了权限 "%current_thread().name)
    se.release()

if __name__ == '__main__':
    thread_list=[]
    for x in  range(20):
        t=Thread(target=do_task,)
        t.start()
        thread_list.append(t)
    for x in thread_list:
        x.join()
