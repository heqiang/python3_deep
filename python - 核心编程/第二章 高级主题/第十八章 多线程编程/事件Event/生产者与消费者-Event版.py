import  threading
import time
import queue


event = threading.Event()
goods = queue.Queue(5)
num = 0

class producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(producer, self).__init__(*args, **kwargs)
    def run(self):
        global  num
        while True:
            if goods.empty():
                event.clear()  #False
                for _ in  range(5):
                    goods.put("商品-"+str(num))
                    print("%s 生产了商品-%d"%(threading.current_thread().name,num))
                    num += 1
                #开始唤醒消费者线程
                event.set()
class  cousumer(threading.Thread):
    def __init__(self,*args,**kwargs):
        super(cousumer,self).__init__(*args,**kwargs)
        self.money = 7

    def run(self):
        while self.money:
            event.wait()
            self.money -= 1
            print("%s购买了-%s"%(threading.current_thread().name,goods.get()))
            time.sleep(1)
        print("{0}没钱了 ，回家".format(threading.current_thread().name))

if __name__ == '__main__':
    p = producer()
    c1 = cousumer(name="hq")
    c2 = cousumer(name="hxj")
    p.start()
    c1.start()
    c2.start()
    c1.join()
    c2.join()