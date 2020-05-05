'''
闭包 三要素
1 有一个内嵌函数
2 内嵌函数引用了外部函数的自由变量
3 返回内嵌函数
'''
# 通过闭包实现平均数
def  average():
    series=[]
    print()
    def averager(new_average):
        print("传进来的参数是：%d"%new_average)
        series.append(new_average)
        total=sum(series)
        return  total/len(series)
    return averager

res=average()
print(res(10))
print(res(12))
#通过类实现平均数
class  average(object):
    def __init__(self):
        self.seies=[]
    def __call__(self, new_value):
        self.seies.append(new_value)
        total=sum(self.seies)
        return total/len(self.seies)

res1=average()
# print(res1(10))
# print(res1(11))