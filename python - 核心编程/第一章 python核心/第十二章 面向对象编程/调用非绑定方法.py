class Anmail(object):
    def __init__(self, color, sex):
        self.color = color
        self.sex = sex
    '''
    当不加 @classmethod  默认该方法为对象绑定的方法 实例对象调用的时候讲  
    通过类的调用则视其为函数的调用 有多少个参数就必须传递多少个参数
    使用@staticmethod 
    '''
    @classmethod
    def bar(self):
        print("get  bar")


dog = Anmail("金毛","女")
dog.bar() #通过对象调用方法
Anmail.bar()
