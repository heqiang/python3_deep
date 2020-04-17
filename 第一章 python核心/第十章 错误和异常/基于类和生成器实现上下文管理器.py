
class FkResource:
    def __init__(self,value):
        self.value=value
        print("初始化构造器:%s"%value)
    def open(self):
        print("开始了")
    def close(self):
        print("结束 关闭")
    def __enter__(self):
        print("Enter方法实现了")
        self.open()
        return self.value,"ok"
    def  __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is  None:
            print("无异常")
            self.close()
            print("准备退出了")
        else:
            print("异常")

with FkResource("tag.txt") as (f,ceshi):
    print(ceshi)
    print(f)

#基于生成器实现的上下文管理器
from contextlib import contextmanager

@contextmanager
def filename(name,mode):
    try:
        f=open(name,mode)
        yield f
    except:
        f.close()
with filename("hhga.txt",'a') as f:
    f.write("写入成功")