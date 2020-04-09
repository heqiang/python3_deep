class Foo:
    __instance = None
    def __init__(self):
        self.ip = '1.2.3.4'
        self.port = 3360
        self.pwd = '123456'
        self.username = 'xxxx'
        self.conn_list = [1,2,3,4,5,6,7,8]
    @classmethod  # 调用类的方法来创建一个单例
    def get_connetion(cls):
        if cls.__instance:
            return cls.__instance
        else:
            cls.__instance = Foo()
            return cls.__instance

obj1 = Foo.get_connetion()
print(obj1)
obj2 = Foo.get_connetion()
print(obj2)