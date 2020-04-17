import  threading
from time import  sleep,ctime

loops=[4,2]

def loop(nloop,nsec):
    print("start loop",nloop,'at:' ,ctime())
    sleep(nsec)
    print("end loop",nloop,'at:' ,ctime())

def main():
    print("starting at :",ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)

    for i in threads: #开始线程
        i.start()
    for i  in threads:
        i.join()
    print("all  done  at :",ctime())

#通过类的