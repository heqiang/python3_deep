import   threading
import time

def run(n):
    lock.acquire()
    global  num
    num += 1
    print("当前线程：%s"%threading.current_thread())
    lock.release()

num = 0
t_obj = []
lock=threading.Lock()


for x in range(200000):
    t=threading.Thread(target=run,args=("t-%s"%x,))
    t.start()
    t_obj.append(t)
for x in t_obj:
    x.join()

print(num)