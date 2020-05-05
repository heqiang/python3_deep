import time
from threading  import Thread

def counter(n):
    while n>0:
        print("T-minus",n)
        n-=1
        time.sleep(1)
print("目前的线程名字是：",Thread.name)
t=Thread(target=counter,args=(10,))
# t.start()
if t.is_alive():
    print('Still running')
else:
    print("Complete")
# t.join()

class CountdownTask:
    def __init__(self):
        self._running = True
    def terminate(self):
        self._running = False
    def run(self,n):
        while self._running and n > 0:
            print("T-minus",n)
            n-=1
            time.sleep(2)


c = CountdownTask()
t = Thread(target=c.run,args=(10,))
t.start()
c.terminate()

