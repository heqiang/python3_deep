map_=map(lambda x: x ** 2, range(6))
# print(map_)
# for x  in map_:
#     print(x)
# print(range(6))
seq = [11, 10, 9, 9, 10, 10, 9, 8, 23, 9, 7, 18, 12, 11, 12]

#lambda表达式 中 视1  或者 true 为符合值 所以x%2 过滤的是偶数
filter_res=filter(lambda  x :x%2,seq)
# for x in filter_res:
# #     print(x)
#需要计算出所有非空白字符的数目
f=open("hhga.txt",'r')
res_split=[word for line in f for word in  line.split()]
f.seek(0)
sum_f=sum([len(word) for line in f for word in line.split() ])

class Number(object):
    def __init__(self,value):
        self.value=value
    def __iadd__(self, increment):
        return  self.value+increment
n=Number(5)
n+=5
print(n)
axis=[[x,y]for x in range(5) for y in range(6)]
print(axis)
f=open("hhga.txt",'r')
res=max(len(x.strip()) for x in f)
print(res)
f.close()
print([x for x in range(-20,861,220)])




