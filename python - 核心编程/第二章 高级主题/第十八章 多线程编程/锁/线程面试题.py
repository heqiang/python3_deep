import  threading
import time

def show1():
    for x  in range(1,52,2):
        lock_show2.acquire()
        print(x,end='')
        print(x+1,end='')
        lock_show1.release()


def show2():
    for x in range(26):
        lock_show1.acquire()
        print(chr(x+ord("A")))
        lock_show2.release()

lock_show1 = threading.Lock()
lock_show2 = threading.Lock()

show1_thread = threading.Thread(target=show1)
show2_thread = threading.Thread(target=show2)


lock_show1.acquire()

show1_thread.start()
show2_thread.start()