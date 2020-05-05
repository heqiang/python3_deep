import threading
from time import sleep,ctime


loops=[4,2]
class ThreaFunc(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
        self.name=name
    def run(self):
         self.func(*self.args)
    # def  __call__(self):
    #      self.func(*self.args)

def loop(nloop,nsec):
    print("start loop",nloop,'at:',ctime())
    sleep(nsec)
    print("end  loop",nloop,'at:',ctime())

def  main():
    print("starting at:"+ctime())
    threads = []
    nloop = range(len(loops))
    for x  in nloop:
        t=target=ThreaFunc(func=loop,args=(x ,loops[x]),name=loop.__name__)
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()

if __name__ == '__main__':
    main()