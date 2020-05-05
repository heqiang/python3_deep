from  multiprocessing import  Process
import time,random

class process_run(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print("%s running "%self.name)
        time.sleep(random.randrange(1.5))
        print("%s running end "%self.name)

t1 = process_run("Jack")
t2 = process_run("hq")
t3 = process_run("xiaoming")
t1.start()
t2.start()
t3.start()
print("Done")
