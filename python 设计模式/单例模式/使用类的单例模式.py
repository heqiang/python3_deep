from time import ctime,sleep
import threading

class Singleton(object):
    __instance=None
    def __init__(self,x):
        self.x=x
        sleep(1)

    def my_single(self,*args,**kwargs):

        if not self.__instance:

            self.__instance=self(*args,**kwargs)
        return self.__instance

a=None
if a:
    print("")
