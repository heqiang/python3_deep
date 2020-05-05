from  functools import wraps

def ceshi(text):
    def log(func):
        #该装饰器注解是为了获取原函数的原信息拷贝到func函数里
        @wraps(func)
        def wrapper(*args,**kwargs):
            print("call %s()"%func.__name__)
            print("args = {}".format(*args))
            print(kwargs)
            print(text)
            return  func(*args,**kwargs)
        return wrapper
    return log

# 以下是通过装饰器的调用方法
date = {"name":"hq"}
@ceshi("hq")
def test(p,**kwargs):
    print(test.__name__ + "parm:"+p)
test("hq",**date)

# 以下是不使用装饰器调用 其本质调用方法
# def test(p,**kwargs):
#     print(test.__name__ + "parm:"+p)
# res = log(test)
# res("hq",**date)
print("***"*50)
def log_with_param(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('call %s():' % func.__name__)
            print('args = {}'.format(*args))
            print('log_param = {}'.format(text))
            return func(*args, **kwargs)

        return wrapper

    return decorator
# @log_with_param("参数")
def tesr_with_param(hq):
      print(hq)
# func = log_with_param("测试1")
# func2 = func(tesr_with_param)
# func2("参数2 ")