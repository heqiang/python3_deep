import  threading
import time

def run(n):
    print("task",n)
    time.sleep(1)

# for x  in range(3):
#     t=threading.Thread(target=run,args=(5,))
#     t.start()

#当主线程休眠的时间过长时，其他线程可能已经结束 所以当前活跃线程数不确定
# time.sleep(0.5)
# print(threading.activeCount())
print("-"*50)
#将子线程设为守护线程
for x in range(3):
    t=threading.Thread(target=run,args=(3,))
    t.setDaemon(True)
    t.start()
time.sleep(0.5)
print(threading.activeCount())