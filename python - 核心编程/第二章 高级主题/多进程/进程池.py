from multiprocessing  import Pool
import  time,random,os

def long_time_task(name):
    print("run task %s  (%s)"%(name,os.getpid()))
    start_time = time.time()
    time.sleep(random.random()*3)
    end_time = time.time()
    print("Task %s runns %0.2f seconds"%(name,(end_time-start_time)))
if __name__ == '__main__':
    print("Partent process (%s)"%(os.getpid()) )
    p=Pool(4)
    for x in range(5):
        p.apply_async(long_time_task,args=(x,))
    print("waiting for all process done ........")
    p.close()
    p.join()
    print("All  process done")