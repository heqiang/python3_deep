astr='ABC'
alist=[1,2,3]
adict={"name":"wangbm","age":18}

agen=(i for i in range(4,8))


def gen(*args, **kw):
   for x in args:
       yield from x


new_list=gen(astr,alist,adict,agen)
print(list(new_list)
      )
total = 0
count = 0
average = 0
# 子生成器
def average_gen():
    global total,count,average
    while True:
        new_num = yield average
        count += 1
        total += new_num
        average = total/count
        return  total,count,average
# 委托生成器
def proxy_gen():
    while True:
      total,count,average = yield from average_gen()
      print("计算完毕！！\n总共传入 {} 个数值， 总和：{}，平均数：{}".format(count, total, average))
# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)            # 预激下生成器
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0

if __name__ == '__main__':
    main()