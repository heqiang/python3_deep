class Foo(object):
    __instance = None
    def __init__(self):
        self.ip = '1.2.3.4'
        self.port = 3360
        self.pwd = '123456'
        self.username = 'xxxx'
        self.conn_list = [1,2,3,4,5,6,7,8]
    # @classmethod  # 调用类的方法来创建一个单例
    @classmethod
    def get_connetion(self):
        if self.__instance:
            return self.__instance
        else:
            self.__instance = Foo()
            return self.__instance

obj1 = Foo.get_connetion()
print(obj1)
obj2 = Foo.get_connetion()
print(obj2)